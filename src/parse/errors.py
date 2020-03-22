def undef(name):
    _halt(f"name \"{name}\" is undefined")

def type_error(target, given, expected):
    _halt(f"\"{target}\" expected to be {expected}, but it was {given}")

def _halt(message):
    print(message)
    exit(1)
