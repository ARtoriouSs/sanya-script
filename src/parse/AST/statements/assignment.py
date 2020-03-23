from parse.AST.statements.statement import Statement


class Assignment(Statement):
    def __init__(self, target, value):
        self.target = target
        self.value = value
