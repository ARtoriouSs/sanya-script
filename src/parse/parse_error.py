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
    def _halt(cls, message):
        print(message)
        exit(1)
