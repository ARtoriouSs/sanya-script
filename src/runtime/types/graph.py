from .type import Type
from ..runtime_error import RuntimeError


class Graph(Type):
    def __init__(self, elements=()):
        self.nodes = set()
        self.arcs = set()
        self.set_elements(list(elements))

    def set_elements(self, elements):
        self._resolve_elements(elements)

    def cast(self, type_):
        if type_ == "graph":
            return self
        else:
            RuntimeError.cast_error("graph", type_)

    def print(self):
        for arc in self.arcs:
            arc.println()
        for i, node in enumerate(self.nodes):
            if i != 0: print(", ", end="")
            node.print()

    def _resolve_elements(self, elements):
        for element in elements:
            if element.__class__.__name__ == "Node":
                self.nodes.add(element)
            elif element.__class__.__name__ == "Arc":
                self._resolve_arc(element)
            elif element.__class__.__name__ == "Graph":
                self._resolve_graph(element)

    def _resolve_arc(self, arc):
        self.arcs.add(arc)
        self.nodes.update([arc.source, arc.target])

    def _resolve_graph(self, graph):
        self.nodes = self.nodes.union(graph.nodes)
        for arc in graph.arcs:
            self._resolve_arc(arc)
