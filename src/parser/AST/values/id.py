from parser.AST.values.value import Value


class Id(Value):
    def __init__(self, name, ret_type, cast=None):
        self.name = name
        self.ret_type = ret_type
        super().__init__(cast)

    def return_type(self):
        return self.cast_type or self.ret_type
