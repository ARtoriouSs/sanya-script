from .runtime_error import RuntimeError


class Graph:
    def __init__(self, elements=()):
        self.nodes = []
        self.arcs = []
        self.set_elements(list(elements))

    def set_elements(self, elements):
        self._resolve_elements(elements)

    def cast(self, type_):
        if type_ == "graph":
            return self
        else:
            RuntimeError.cast_error("graph", type_)

    def print(self):
        pass

    def _resolve_elements(self, elements):
        for element in elements:
            if element.__class__.__name__ == "Node":
                self.nodes.append(element)
            elif element.__class__.__name__ == "Arc":
                self.arcs.append(element)
            elif element.__class__.__name__ == "Graph":
                self._resolve_graph(element)


    def _resolve_graphs(self, graph):
        self.nodes += graph.nodes
        self.arcs += graph.arcs
