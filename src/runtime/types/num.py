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
        from .logic import Logic

        if type_ == "num":
            return self
        elif type_ == "node":
            return Node(self.value)
        elif type_ == "graph":
            return Graph(tuple([Node(self.value)]))
        elif type_ == "logic":
            return Logic(True)
        else:
            RuntimeError.cast_error("num", type_)

    def print(self):
        print(self.value)

    def summation(self, value):
        return self.__class__(self.value + value.value)

    def subtraction(self, value):
        return self.__class__(self.value - value.value)

    def multiplication(self, value):
        return self.__class__(self.value * value.value)

    def division(self, value):
        return self.__class__(self.value / value.value)
