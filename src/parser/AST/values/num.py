from parser.AST.values.value import Value


class Num(Value):
    def __init__(self, value, cast=None):
        self.value = float(value)
        super().__init__(cast)
