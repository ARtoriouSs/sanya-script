from parser.AST.statements.statement import Statement


class PushToArray(Statement):
    def __init__(self, name, value):
        self.name = name
        self.value = value
