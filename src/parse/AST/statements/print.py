from parse.AST.statements.statement import Statement


class Print(Statement):
    def __init__(self, name):
        self.name = name
