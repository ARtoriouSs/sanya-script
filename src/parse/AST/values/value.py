import re

class Value:
    def __init__(self, cast_type=None):
        self.cast_type = cast_type

    def kind(self):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', self.__class__.__name__).lower()

    def cast(self, cast_type=None):
        self.cast_type = cast_type
        return self
