from parse.AST.values.value import Value


class FunCall(Value):
    def __init__(self, name, args = ()):
        self.name = name
        self.args = list(args)
