from parser.AST.statements.statement import Statement


class Deffun(Statement):
    def __init__(self, ret_type, name, args, body):
        self.ret_type = ret_type
        self.name = name
        self.args = args
        self.body = body
