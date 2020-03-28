from parse.AST.statements.statement import Statement


class FunCall(Statement):
    def __init__(self, name, return_type=None, args=()):
        self.name = name
        self.return_type = return_type
        self.args = list(args)
