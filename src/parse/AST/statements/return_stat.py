from parse.AST.statements.statement import Statement


class ReturnStat(Statement):
    def __init__(self, value):
        self.value = value
