from .type import Type
from .graph import Graph
from ..runtime_error import RuntimeError


class Arc(Type):
    def __init__(self, source=None, target=None, weight=0.0, type_="directed"):
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

    def setTarget(self, target):
        self.target = target
        return self

    def cast(self, type_):
        from .num import Num
        from .logic import Logic

        if type_ == "arc":
            return self
        elif type_ == "graph":
            return Graph(tuple([self]))
        elif type_ == "num":
            return Num(self.weight)
        elif type_ == "logic":
            return Logic(True) if self.source and self.target else Logic(False)
        else:
            RuntimeError.cast_error("arc", type_)

    def put(self):
        self.source.put()
        print(f" {'<' if not self._is_directed else ''}-[{self.weight}]-> ", end="")
        self.target.put()

    def summation(self, value):
        return self.__class__(self.weight + value.value)

    def subtraction(self, value):
        return self.__class__(self.weight - value.value)

    def multiplication(self, value):
        return self.__class__(self.weight * value.value)

    def division(self, value):
        return self.__class__(self.weight / value.value)

    def greater_or_equal(self, value):
        from .logic import Logic
        return Logic(self.weight >= value.cast("arc").weight)

    def less_or_equal(self, value):
        from .logic import Logic
        return Logic(self.weight <= value.cast("arc").weight)

    def greater(self, value):
        from .logic import Logic
        return Logic(self.weight > value.cast("arc").weight)

    def less(self, value):
        from .logic import Logic
        return Logic(self.weight < value.cast("arc").weight)

    def _is_directed(self):
        return True if self.type == "directed" else False
