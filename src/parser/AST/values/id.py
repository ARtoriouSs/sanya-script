from parser.AST.values.value import Value


class Id(Value):
    def __init__(self, name, return_type, cast=None):
        self.name = name
        self.return_type = return_type
        super().__init__(cast)

    def return_type(self):
        return self.cast_type or self.return_type
