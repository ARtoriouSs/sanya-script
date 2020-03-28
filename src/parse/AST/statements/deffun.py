from parse.AST.statements.statement import Statement


class Deffun(Statement):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body
