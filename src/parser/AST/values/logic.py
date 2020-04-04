from parser.AST.values.value import Value


class Logic(Value):
    def __init__(self, value, cast=None):
        self.value = bool(value)
        super().__init__(cast)
