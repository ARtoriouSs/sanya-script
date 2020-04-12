from parser.AST.statements.statement import Statement


class FunCall(Statement):
    def __init__(self, fun, args=()):
        self.fun = fun
        self.name = fun.name
        self.return_type = fun.return_type
        self.args = list(args)
