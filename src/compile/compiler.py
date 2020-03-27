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
            elif statement.kind() == "return_stat":
                self._compile_return_stat(statement)

    def _indent(self):
        return "    " * self.tab_spot

    def _compile_defvar(self, statement):
        self.file.write(f"{statement.name} = {statement.type.capitalize()}()\n")

    def _compile_print(self, statement):
        self.file.write(f"{statement.name}.print()\n")

    def _compile_assignment(self, statement):
        self.file.write(f"{statement.target.name} = {self._resolve_value(statement.value)}\n")

    def _compile_return_stat(self, statement):
        self.file.write(f"return {self._resolve_value(statement.value)}\n")

    def _resolve_value(self, value):
        if value.kind() == "id":
            string = value.name
        elif value.kind() == "node":
            string = f"Node({value.value})"
        elif value.kind() == "arc":
            string = f"Arc({self._resolve_value(value.source)}, {self._resolve_value(value.target)}, {value.weight}, \"{value.type}\")"
        elif value.kind() == "graph":
            string = self._resolve_graph_value(value)
        string += f".cast(\"{value.cast_type}\")" if value.cast_type else ""
        return string

    def _resolve_graph_value(self, value):
        return f"Graph([{self._resolve_array(value.elements)}])"

    def _resolve_array(self, values):
        result = ""
        for i, value in enumerate(values):
            if not i == 0: result += ", "
            result += self._resolve_value(value)
        return result

