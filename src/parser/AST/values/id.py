import re

from parser.AST.values.value import Value


class Id(Value):
    def __init__(self, var, cast=None, index=None):
        self.var = var
        self.name = var.name
        self.ret_type = var.type
        super().__init__(cast, index)

    def return_type(self):
        return self.cast_type or self._return_type_with_index()

    def _return_type_with_index(self):
        return self.ret_type if self.index is None else re.sub("{}", "", self.ret_type)
