class Compiler:
    def __init__(self, targer):
        self.file = open(targer, "w+")
        self.file.write("from lxml import etree\n")
        self.tab_spot = 0

    def compile(self, ast):
        for statement in ast.statements:
            if statement.kind() == "defvar":
                pass
            elif statement.kind() == "print":
                pass

    def _indent(self):
        return "    " * self.tab_spot
