class ParseError:
    @classmethod
    def undef(cls, name):
        cls._halt(f"name \"{name}\" is undefined")

    @classmethod
    def type_error(cls, target, given, expected):
        cls._halt(f"\"{target}\" expected to be {expected}, but it was {given}")

    @classmethod
    def array_value_error(cls, target, given, expected):
        cls._halt(f"{given} is pushed to \"{target}\" wich is {expected}")

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
    def incompatible_unary_operation(cls, operation, target):
        cls._halt(f"operation {operation} cannot be performed with {target}")

    @classmethod
    def cycle_enumerator_error(cls, given):
        cls._halt(f"cycle argument must be an array, but {given} given")

    @classmethod
    def index_error(cls, name, given):
        cls._halt(f"index for {name} must be num, but {given} given")

    @classmethod
    def for_to_type_error(cls):
        cls._halt("for-to cycle arguments must both be num")

    @classmethod
    def _halt(cls, message):
        print(message)
        exit(1)
