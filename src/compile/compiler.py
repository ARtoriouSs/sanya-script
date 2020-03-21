class Compiler:
    def __init__(self, targer):
        self.file = open(targer, "w+")
        self.file.write("from runtime import *\n")
        self.tab_spot = 0

    def compile(self, ast):
        for statement in ast.statements:
            if statement.kind() == "defvar":
                self._write_defvar(statement)
            elif statement.kind() == "print":
                self._write_print(statement)

    def _indent(self):
        return "    " * self.tab_spot

    def _write_defvar(self, statement):
        self.file.write(f"{statement.name} = {statement.type.capitalize()}()\n")

    def _write_print(self, statement):
        self.file.write(f"{statement.name}.print()\n")
