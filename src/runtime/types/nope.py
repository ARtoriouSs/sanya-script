from .type import Type
from .num import Num
from ..runtime_error import RuntimeError


class Nope(Type):
    def cast(self, type_):
        RuntimeError.cast_error("nope", type_)

    def print(self):
        print("nope")
