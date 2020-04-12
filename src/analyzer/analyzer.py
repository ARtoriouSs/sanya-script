import re

from parser.compilation_error import CompilationError
from analyzer.value_analyzer import ValueAnalyzer


class Analyzer:
    def validate(self, ast):
        for statement in ast.statements:
            self.current_line = statement.line
            self._check(statement)
        return True

    def _check(self, statement):
        if statement.kind() == "defvar":
            self._check_defvar(statement)
        elif statement.kind() == "deffun":
            self._check_deffun(statement)
        elif statement.kind() == "assignment":
            self._check_assignment(statement)
        elif statement.kind() == "return_stat":
            self._check_return_stat(statement)
        elif statement.kind() == "fun_call":
            self._check_fun_call(statement)
        elif statement.kind() == "if_stat":
            self._check_if_stat(statement)
        elif statement.kind() == "for_in_cycle":
            self._check_for_in_cycle(statement)
        elif statement.kind() == "for_to_cycle":
            self._check_for_to_cycle(statement)
        elif statement.kind() == "while_cycle":
            self._check_while_cycle(statement)
        elif statement.kind() == "push_to_array":
            self._check_push_to_array(statement)

    def _check_defvar(self, statement):
        pass

    def _check_deffun(self, statement):
        arg_names = [arg.name for arg in statement.args]
        if len(arg_names) != len(set(arg_names)):
            self._error().duplicate_args(statement.name)

        self.validate(statement.body)

    def _check_assignment(self, statement):
        target = statement.target
        value = statement.value

        self._value_analyzer().validate(value)

        if target.undef: self._error().undef(target.name)
        if target.is_const: self._error().const_reassignment(target.name)
        if target.type != value.return_type() and value.return_type() != "nope":
            self._error().type_error(target.name, value.return_type(), target.type)

    def _check_return_stat(self, statement):
        self._value_analyzer().validate(statement.value)

    def _check_fun_call(self, statement):
        if statement.fun.undef:
            self._error().signature_not_found(statement.name, statement.args)

        for arg in statement.args:
            self._value_analyzer().validate(arg)

    def _check_if_stat(self, statement):
        self._value_analyzer().validate(statement.condition)
        self.validate(statement.then)
        if statement.else_ is not None: self.validate(statement.else_)

    def _check_for_in_cycle(self, statement):
        var = statement.target
        enumerable = statement.enumerable

        self._value_analyzer().validate(enumerable)

        if not re.match(r".*{}", enumerable.return_type()):
            self._error().cycle_enumerator_error(enumerable.return_type())
        if var.type + "{}" != enumerable.return_type():
            self._error().type_error(var.name, var.type, re.sub("{}", "", enumerable.return_type()))

        self.validate(statement.block)

    def _check_for_to_cycle(self, statement):
        self._value_analyzer().validate(statement.to)

        if statement.to.return_type() != "num" or statement.target.type != "num":
            self._error().for_to_type_error()

        self.validate(statement.block)

    def _check_while_cycle(self, statement):
        self._value_analyzer().validate(statement.condition)
        self.validate(statement.block)

    def _check_push_to_array(self, statement):
        target = statement.target
        value = statement.value

        self._value_analyzer().validate(value)

        if target.undef: self._error().undef(target.name)
        if target.type != value.return_type() + "{}" and value.return_type() != "nope":
            self._error().array_value_error(target.name, value.return_type(), target.type)

    def _value_analyzer(self):
        return ValueAnalyzer(self._error())

    def _error(self):
        return CompilationError(self.current_line)
