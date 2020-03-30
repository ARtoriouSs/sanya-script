from parser.AST.statements.statement import Statement


class Println(Statement):
    def __init__(self, value):
        self.value = value
