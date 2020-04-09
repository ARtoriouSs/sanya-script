from parser.AST.statements.statement import Statement


class WhileCycle(Statement):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
