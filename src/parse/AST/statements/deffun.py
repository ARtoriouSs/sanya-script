from parse.AST.statements.statement import Statement


class Deffun(Statement):
    def __init__(self, return_type, name, args, body):
        self.return_type = return_type
        self.name = name
        self.args = args
        self.body = body
