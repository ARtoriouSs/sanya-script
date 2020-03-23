class Compiler:
    def __init__(self, targer):
        self.file = open(targer, "w+")
        self.file.write("from src.runtime import *\n")
        self.tab_spot = 0

    def compile(self, ast):
        for statement in ast.statements:
            if statement.kind() == "defvar":
                self._compile_defvar(statement)
            elif statement.kind() == "print":
                self._compile_print(statement)
            elif statement.kind() == "assignment":
                self._compile_assignment(statement)

    def _indent(self):
        return "    " * self.tab_spot

    def _compile_defvar(self, statement):
        self.file.write(f"{statement.name} = {statement.type.capitalize()}()\n")

    def _compile_print(self, statement):
        self.file.write(f"{statement.name}.print()\n")

    def _compile_assignment(self, statement):
        self.file.write(f"{statement.target.name} = {self._resolve_value(statement.value)}\n")

    # TODO: casts (on runtime objects?)
    def _resolve_value(self, value):
        if value.kind() == "id":
            return value.name
        elif value.kind() == "node":
            return f"Node({value.value})"
        elif value.kind() == "arc":
            return f"Arc({self._resolve_value(value.source)}, {self._resolve_value(value.target)}, {value.weight}, \"{value.type}\")"
