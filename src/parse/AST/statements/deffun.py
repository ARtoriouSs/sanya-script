from parse.AST.statements.statement import Statement


class Defvar(Statement):
    def __init__(self, return_type, name):
        self.return_type = return_type
        self.name = name
