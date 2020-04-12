from parser.AST.statements.statement import Statement


class ForInCycle(Statement):
    def __init__(self, target, enumerable, block):
        self.target = target
        self.enumerable = enumerable
        self.block = block
