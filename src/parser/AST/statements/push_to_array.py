from parser.AST.statements.statement import Statement


class PushToArray(Statement):
    def __init__(self, target, value):
        self.target = target
        self.value = value
