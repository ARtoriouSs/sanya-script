def undef(name):
    _halt(f"name \"{name}\" is undefined")

def type_error(target, given, expected):
    _halt(f"\"{target}\" expected to be {expected}, but it was {given}")

def signature_not_found(name, arg_types):
    _halt(f"function with name \"{name}\" and args ({', '.join(arg_types)}) is undefined")

def _halt(message):
    print(message)
    exit(1)
