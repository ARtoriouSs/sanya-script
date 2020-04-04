class ParseError:
    @classmethod
    def undef(cls, name):
        cls._halt(f"name \"{name}\" is undefined")

    @classmethod
    def type_error(cls, target, given, expected):
        cls._halt(f"\"{target}\" expected to be {expected}, but it was {given}")

    @classmethod
    def signature_not_found(cls, name, arg_types):
        cls._halt(f"function with name \"{name}\" and args ({', '.join(arg_types)}) is undefined")

    @classmethod
    def arc_error(cls, given):
        cls._halt(f"only nodes can be a part of arc, but {given} given")

    @classmethod
    def incompatible_operation(cls, operation, left, right):
        cls._halt(f"operation {operation} cannot be performed with {left} and {right}")

    @classmethod
    def _halt(cls, message):
        print(message)
        exit(1)
