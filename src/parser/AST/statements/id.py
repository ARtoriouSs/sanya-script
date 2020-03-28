from parser.AST.statements.statement import Statement


class Id(Statement):
    def __init__(self, name):
        self.name = name
