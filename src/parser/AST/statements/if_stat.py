from parser.AST.statements.statement import Statement


class IfStat(Statement):
    def __init__(self, condition, then, else_=None):
        self.condition = condition
        self.then = then
        self.else_ = else_
