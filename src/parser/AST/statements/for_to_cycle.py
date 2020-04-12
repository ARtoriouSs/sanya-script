from parser.AST.statements.statement import Statement


class ForToCycle(Statement):
    def __init__(self, target, to, block):
        self.target = target
        self.to = to
        self.block = block
