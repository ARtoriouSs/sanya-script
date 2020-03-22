from parse.AST.statements.statement import Statement


class Assignment(Statement):
    def __init__(self, target, value, cast):
        self.target = target
        self.value = value
        self.cast = cast
