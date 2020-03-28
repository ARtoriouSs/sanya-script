from parse.AST.values.value import Value


class FunCall(Value):
    def __init__(self, fun_call, cast=None):
        self.fun_call = fun_call
        super().__init__(cast)
