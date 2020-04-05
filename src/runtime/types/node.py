from .type import Type
from .graph import Graph
from ..runtime_error import RuntimeError


class Node(Type):
    def __init__(self, value=0.0):
        self.value = value

    def setValue(self, value):
        self.value = value
        return self

    def cast(self, type_):
        from .num import Num
        from .logic import Logic

        if type_ == "node":
            return self
        elif type_ == "graph":
            return Graph(tuple([self]))
        elif type_ == "num":
            return Num(self.value)
        elif type_ == "logic":
            return Logic(True)
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

    def greater_or_equal(self, value):
        from .logic import Logic
        return Logic(self.value >= value.cast("node").value)

    def less_or_equal(self, value):
        from .logic import Logic
        return Logic(self.value <= value.cast("node").value)

    def greater(self, value):
        from .logic import Logic
        return Logic(self.value > value.cast("node").value)

    def less(self, value):
        from .logic import Logic
        return Logic(self.value < value.cast("node").value)
