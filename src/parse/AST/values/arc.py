from parse.AST.values.value import Value


class Arc(Value):
    def __init__(self, source, target, weight = 42, type_ = "undirected"):
        self.source = source
        self.target = target
        self.type = type_
        self.weight = weight
