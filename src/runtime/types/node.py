from .type import Type
from .graph import Graph
from .num import Num
from ..runtime_error import RuntimeError


class Node(Type):
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
        elif type_ == "num":
            return Num(self.value)
        else:
            RuntimeError.cast_error("node", type_)

    def print(self):
        print(f"^{self.value}", end='')

    def summation(self, value):
        return self.__class__(self.value + value.value)

    def subtraction(self, value):
        return self.__class__(self.value - value.value)

    def multiplication(self, value):
        return self.__class__(self.value * value.value)

    def division(self, value):
        return self.__class__(self.value / value.value)
