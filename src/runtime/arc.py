from .graph import Graph
from .runtime_error import RuntimeError


class Arc:
    def __init__(self, source=None, target=None, weight=0, type_="directed"):
        self.source = source
        self.target = target
        self.weight = weight
        self.type = type_

    def setWeight(self, weight):
        self.weight = weight
        return self

    def setType(self, type_):
        self.type = type_
        return self

    def setSource(self, source):
        self.source = source
        return self

    def setTarger(self, target):
        self.target = target
        return self

    def cast(self, type_):
        if type_ == "arc":
            return self
        elif type_ == "graph":
            return Graph(tuple([self]))
        else:
            RuntimeError.cast_error("arc", type_)

    def print(self):
        print(f"{self.source.value} {'<' if not self._is_directed else ''}-[{self.weight}]-> {self.target.value}")

    def _is_directed(self):
        return True if self.type == "directed" else False
