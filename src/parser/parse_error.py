class ParseError:
    def __init__(self, line=None):
        self.line_prefix = f"line: {line}" if line is not None else ""

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
    def signature_not_found(cls, name, args):
        cls._halt(f"function with name \"{name}\" and args ({', '.join(cls._arg_types(args))}) is undefined")

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
    def for_to_type_error(cls):
        cls._halt("for-to cycle arguments must both be num")

    @classmethod
    def const_reassignment(cls, name):
        cls._halt(f"reassignment of const {name} not allowed")

    @classmethod
    def cannot_be_indexed(cls, type_):
        cls._halt(f"value of type {type_} cannot be indexed, only arrays allowed")

    @classmethod
    def incorrect_index_type(cls, type_):
        cls._halt(f"value of type {type_} cannot be used as index, only num allowed")

    @classmethod
    def duplicate_args(cls, name):
        cls._halt(f"duplicate argument name in fun {name} definition")

    @classmethod
    def _halt(cls, message):
        print(message)
        exit(1)

    @classmethod
    def _arg_types(self, args):
        return [arg.return_type() for arg in args]
