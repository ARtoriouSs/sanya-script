from parser.AST.statements.statement import Statement


class ForToCycle(Statement):
    def __init__(self, var_name, to, block):
        self.var_name = var_name
        self.to = to
        self.block = block
