from parser.AST.values.value import Value


class Graph(Value):
    def __init__(self, elements=(), cast=None):
        self.elements = list(elements)
        super().__init__(cast)
