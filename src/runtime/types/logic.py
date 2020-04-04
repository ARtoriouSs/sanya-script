from .type import Type
from .num import Num
from ..runtime_error import RuntimeError


class Logic(Type):
    def __init__(self, value):
        self.value = bool(value)

    def setValue(self, value):
        self.value = bool(value)
        return self

    def cast(self, type_):
        if type_ == "num":
            return Num(1.0) if self.value else Num(0.0)
        else:
            RuntimeError.cast_error("logic", type_)

    def print(self):
        string = "yes" if self.value else "no"
        print(string)
