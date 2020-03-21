from parse.AST.statements.statement import Statement


class Defvar(Statement):
    def __init__(self, type, name):
        self.type = type
        self.name = name
