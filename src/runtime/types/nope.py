from .type import Type
from ..runtime_error import RuntimeError


class Nope(Type):
    def cast(self, type_):
        from .logic import Logic

        if type_ == "logic":
            return Logic(False)
        else:
            RuntimeError.cast_error("nope", type_)

    def put(self):
        print("nope")
