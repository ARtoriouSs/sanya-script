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
        from .logic import Logic

        if type_ == "graph":
            return self
        elif type_ == "logic":
            return Logic(True)
        else:
            RuntimeError.cast_error("graph", type_)

    def all_elements(self):
        return self.nodes.union(self.arcs)

    def put(self):
        for arc in self.arcs:
            arc.puts()
        for i, node in enumerate(self.nodes):
            if i != 0: print(", ", end="")
            node.put()

    def summation(self, value):
        return self.__class__(self.all_elements().union(value.all_elements()))

    def subtraction(self, value):
        return self.__class__(self.all_elements().difference(value.all_elements()))

    # TODO: operations
    def multiplication(self, value):
        pass

    def division(self, value):
        pass

    def greater_or_equal(self, value):
        from .logic import Logic

    def less_or_equal(self, value):
        from .logic import Logic

    def greater(self, value):
        from .logic import Logic

    def less(self, value):
        from .logic import Logic

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
