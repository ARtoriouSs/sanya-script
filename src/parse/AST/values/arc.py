from parse.AST.values.value import Value


class Arc(Value):
    def __init__(self, start, end, weight = 42, type = "undirected"):
        self.start = start
        self.end = end
        self.type = type
        self.weight = weight
