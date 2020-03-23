from parse.AST.values.value import Value


class Graph(Value):
    def __init__(self, nodes = [], arcs = [], cast = None):
        self.nodes = nodes
        self.arcs = arcs
        super().__init__(cast)

    def merge(self, graph):
        self.nodes += graph.nodes
        self.arcs += graph.arcs
