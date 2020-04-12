import re


class Value:
    def __init__(self, cast_type=None, index=None):
        self.cast_type = cast_type
        self.index = index

    def kind(self):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.__class__.__name__).lower()

    def cast(self, cast_type=None):
        self.cast_type = cast_type
        return self

    def set_index(self, index_):
        self.index = index_
        return self

    def return_type(self):
        return self.cast_type or self.kind()
