from parse.AST.values.value import Value


class FunCall(Value):
    def __init__(self, fun_call, return_type, cast=None):
        self.fun_call = fun_call
        self.return_type = return_type
        super().__init__(cast)

    def return_type(self):
        return self.return_type
