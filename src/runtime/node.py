from .graph import Graph
from .runtime_error import RuntimeError


class Node:
    def __init__(self, value=0.0):
        self.value = value

    def setValue(self, value):
        self.value = value
        return self

    def cast(self, type_):
        if type_ == "node":
            return self
        elif type_ == "graph":
            return Graph(tuple([self]))
        else:
            RuntimeError.cast_error("node", type_)

    def print(self):
        print(f"^{self.value}", end='')

    def println(self):
        self.print()
        print()
