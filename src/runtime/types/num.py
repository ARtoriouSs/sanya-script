from .type import Type
from .graph import Graph
from .node import Node
from ..runtime_error import RuntimeError


class Num(Type):
    def __init__(self, value=0.0):
        self.value = value

    def setValue(self, value):
        self.value = value
        return self

    def cast(self, type_):
        if type_ == "node":
            return Node(self.value)
        elif type_ == "graph":
            return Graph(tuple([Node(self.value)]))
        else:
            RuntimeError.cast_error("num", type_)

    def print(self):
        print(self.value)
