import re

from parser.parse_error import ParseError


class Analyzer:
    def __init__(self, ast):
        self.ast = ast

    def validate(self):
        for statement in self.ast.statements:
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
            ParseError.duplicate_args(statement.name)

    def _check_assignment(self, statement):
        target = statement.target
        value = statement.value

        if target.undef: ParseError.undef(target.name)
        if target.is_const: ParseError.const_reassignment(target.name)
        if target.type != value.return_type() and value.return_type() != "nope":
            ParseError.type_error(target.name, value.return_type(), target.type)

    def _check_return_stat(self, statement):
        pass

    def _check_fun_call(self, statement):
        if statement.fun.undef:
            ParseError.signature_not_found(statement.name, statement.args)

    def _check_if_stat(self, statement):
        pass

    def _check_for_in_cycle(self, statement):
        var = statement.target
        enumerable = statement.enumerable

        if not re.match(r".*{}", enumerable.return_type()):
            ParseError.cycle_enumerator_error(enumerable.return_type())
        if var.type + "{}" != enumerable.return_type():
            ParseError.type_error(var.name, var.type, re.sub("{}", "", enumerable.return_type()))

    def _check_for_to_cycle(self, statement):
        if statement.to.return_type() != "num" or statement.target.type != "num":
            ParseError.for_to_type_error()

    def _check_while_cycle(self, statement):
        pass

    def _check_push_to_array(self, statement):
        target = statement.target
        value = statement.value

        if target.undef: ParseError.undef(target.name)
        if target.type != value.return_type() + "{}" and value.return_type() != "nope":
            ParseError.array_value_error(target.name, value.return_type(), target.type)
