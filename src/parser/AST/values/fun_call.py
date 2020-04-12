import re

from parser.AST.values.value import Value


class FunCall(Value):
    def __init__(self, fun_call, cast=None, index=None):
        self.fun_call = fun_call
        super().__init__(cast, index)

    def return_type(self):
        return self.cast_type or self._return_type_with_index()

    def _return_type_with_index(self):
        return self.fun_call.return_type if self.index is None else re.sub("{}", "", self.fun_call.return_type)
