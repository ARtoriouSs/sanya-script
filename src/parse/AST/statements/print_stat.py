from parse.AST.statements.statement import Statement


class PrintStat(Statement):
    def __init__(self, value):
        self.value = value
