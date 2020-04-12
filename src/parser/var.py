class Var:
    def __init__(self, type_, name, is_const=False, undef=False):
        self.type = type_
        self.name = name
        self.is_const = is_const
        self.undef = undef
