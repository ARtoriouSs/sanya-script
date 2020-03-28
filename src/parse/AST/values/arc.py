from parse.AST.values.value import Value


class Arc(Value):
    def __init__(self, source, target, weight=0, type_="undirected", cast = None):
        self.source = source
        self.target = target
        self.type = type_
        self.weight = weight
        super().__init__(cast)
