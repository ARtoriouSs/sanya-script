from parse.AST.values.value import Value


class Graph(Value):
    def __init__(self, nodes=[], arcs=[], graphs=[], cast=None):
        self.nodes = nodes # []
        self.arcs = arcs
        self.graphs = graphs
        super().__init__(cast)
