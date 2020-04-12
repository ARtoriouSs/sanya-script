from parser.AST.values.value import Value


class Id(Value):
    def __init__(self, name, ret_type, index=None, cast=None):
        self.name = name
        self.index = index
        self.ret_type = ret_type
        super().__init__(cast)

    def return_type(self):
        return self.cast_type or self._return_type_with_index()

    def _return_type_with_index(self):
        return self.ret_type if self.index is None else re.sub("{}", "", self.ret_type)
