from .runtime_error import RuntimeError


class Graph:
    def __init__(self, nodes=[], arcs=[]):
        self.arcs = arcs
        self.nodes = nodes

    def setNodes(self, nodes):
        self.nodes = nodes
        return self

    def setArcs(self, arcs):
        self.arcs = arcs
        return self

    def cast(self, type_):
        if type_ == "graph":
            return self
        else:
            RuntimeError.cast_error("graph", type_)

    def print(self):
        print(self.value)
