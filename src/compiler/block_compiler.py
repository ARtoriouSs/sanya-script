import re

from compiler.value_resolver import ValueResolver


class BlockCompiler:
    def __init__(self, target, indent=0):
        self.file = target
        self.indent = indent

    def compile(self, ast):
         for statement in ast.statements:
            self.file.write("    " * self.indent)
            if statement.kind() == "defvar":
                self._compile_defvar(statement)
            elif statement.kind() == "assignment":
                self._compile_assignment(statement)
            elif statement.kind() == "return_stat":
                self._compile_return_stat(statement)
            elif statement.kind() == "deffun":
                self._compile_deffun(statement)
            elif statement.kind() == "fun_call":
                self._compile_fun_call(statement)
            elif statement.kind() == "if_stat":
                self._compile_if(statement)
            elif statement.kind() == "push_to_array":
                self._compile_push_to_array(statement)
            elif statement.kind() == "for_in_cycle":
                self._compile_for_in_cycle(statement)
            elif statement.kind() == "for_to_cycle":
                self._compile_for_to_cycle(statement)
            elif statement.kind() == "while_cycle":
                self._compile_while_cycle(statement)

    def _compile_defvar(self, statement):
        self.file.write(f"{statement.name} = ")
        if statement.is_array():
            self.file.write("[]\n")
        else:
            self.file.write(f"{statement.type.capitalize()}()\n")

    def _compile_assignment(self, statement):
        self.file.write(f"{statement.target.name} = {self._resolve_value(statement.value)}\n")

    def _compile_return_stat(self, statement):
        self.file.write(f"return {self._resolve_value(statement.value)}\n")

    def _compile_deffun(self, statement):
        self.file.write(f"def {statement.name}({self._resolve_fun_args(statement.args)}):\n")
        self._compile_nested_block(statement.body)

    def _compile_fun_call(self, statement):
        self.file.write(f"{statement.name}({self._resolve_array(statement.args)})\n")

    def _compile_if(self, statement):
        self.file.write(f"if {self._resolve_value(statement.condition)}.cast('logic').value:\n")
        self._compile_nested_block(statement.then)
        if statement.else_ is not None:
            self.file.write("    " * self.indent + f"else:\n")
            self._compile_nested_block(statement.else_)

    def _compile_while_cycle(self, statement):
        self.file.write(f"while {self._resolve_value(statement.condition)}.cast('logic').value:\n")
        self._compile_nested_block(statement.block)

    def _compile_for_in_cycle(self, statement):
        self.file.write(f"for {statement.target.name} in {self._resolve_value(statement.enumerable)}:\n")
        self._compile_nested_block(statement.block)

    def _compile_for_to_cycle(self, statement):
        self.file.write(f"for {statement.target.name} in range(int({self._resolve_value(statement.to)}.value)):\n")
        self.file.write("    " * self.indent + f"    {statement.target.name} = Num({statement.target.name})\n")
        self._compile_nested_block(statement.block)

    def _compile_push_to_array(self, statement):
        self.file.write(f"{statement.target.name}.append({self._resolve_value(statement.value)})\n")

    def _compile_nested_block(self, block):
        if any(block.statements):
            self.__class__(self.file, self.indent + 1).compile(block)
        else:
            self.file.write(f"    pass\n")

    def _resolve_value(self, value):
        return ValueResolver().resolve(value)

    def _resolve_fun_args(self, args):
        args = [arg.name for arg in args]
        return ", ".join(args)

    def _resolve_array(self, values):
        values_ = [self._resolve_value(value) for value in values]
        return ", ".join(values_)
