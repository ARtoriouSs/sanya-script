from parser.AST.statements.statement import Statement


class Defvar(Statement):
    def __init__(self, type_, name):
        self.type = type_
        self.name = name
