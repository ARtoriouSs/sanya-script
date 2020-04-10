from parser.AST.statements.statement import Statement


class ForInCycle(Statement):
    def __init__(self, var_name, enumerable, block):
        self.var_name = var_name
        self.enumerable = enumerable
        self.block = block
