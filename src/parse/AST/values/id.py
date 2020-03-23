from parse.AST.values.value import Value


class Id(Value):
    def __init__(self, name, cast = None):
        self.name = name
        super().__init__(cast)
