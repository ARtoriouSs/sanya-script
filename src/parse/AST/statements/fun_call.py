from parse.AST.statements.statement import Statement


class FunCall(Statement):
    def __init__(self, name, args = ()):
        self.name = name
        self.args = list(args)
