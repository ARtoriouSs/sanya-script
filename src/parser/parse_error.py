class ParseError:
    def __init__(self, line=None):
        self.line_prefix = f"Line: {line}: " if line is not None else ""

    def undef(self, name):
        self._halt(f"name \"{name}\" is undefined")

    def type_error(self, target, given, expected):
        self._halt(f"\"{target}\" expected to be {expected}, but it was {given}")

    def array_value_error(self, target, given, expected):
        self._halt(f"{given} is pushed to \"{target}\" wich is {expected}")

    def signature_not_found(self, name, args):
        self._halt(f"function with name \"{name}\" and args ({', '.join(self._arg_types(args))}) is undefined")

    def arc_error(self, given):
        self._halt(f"only nodes can be a part of arc, but {given} given")

    def incompatible_operation(self, operation, left, right):
        self._halt(f"operation {operation} cannot be performed with {left} and {right}")

    def incompatible_unary_operation(self, operation, target):
        self._halt(f"operation {operation} cannot be performed with {target}")

    def cycle_enumerator_error(self, given):
        self._halt(f"cycle argument must be an array, but {given} given")

    def for_to_type_error(self):
        self._halt("for-to cycle arguments must both be num")

    def const_reassignment(self, name):
        self._halt(f"reassignment of const {name} not allowed")

    def cannot_be_indexed(self, type_):
        self._halt(f"value of type {type_} cannot be indexed, only arrays allowed")

    def incorrect_index_type(self, type_):
        self._halt(f"value of type {type_} cannot be used as index, only num allowed")

    def duplicate_args(self, name):
        self._halt(f"duplicate argument name in fun {name} definition")

    def _halt(self, message):
        print(self.line_prefix + message)
        print("Compilation failed!")
        exit(1)

    def _arg_types(self, args):
        return [arg.return_type() for arg in args]
