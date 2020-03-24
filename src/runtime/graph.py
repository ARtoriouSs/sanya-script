from .runtime_error import RuntimeError


class Graph:
    def __init__(self, nodes=[], arcs=[], graphs=[]):
        self.arcs = arcs
        self.nodes = nodes
        self._resolve_graphs(graphs)

    def setNodes(self, nodes):
        self.nodes = nodes
        return self

    def setArcs(self, arcs):
        self.arcs = arcs
        return self

    def setGraphs(self, graphs):
        self._resolve_graphs(graphs)
        return self

    def cast(self, type_):
        if type_ == "graph":
            return self
        else:
            RuntimeError.cast_error("graph", type_)

    def print(self):
        print(self.value)

    def _resolve_graphs(self, graphs):
        for graph in graphs:
            self.nodes += graph.nodes
            self.arcs += graph.arcs
