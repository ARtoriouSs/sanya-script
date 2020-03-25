from parse.AST.values.value import Value


class Graph(Value):
    def __init__(self, nodes=(), arcs=(), graphs=(), cast=None):
        self.nodes = list(nodes)
        self.arcs = list(arcs)
        self.graphs = list(graphs)
        super().__init__(cast)
