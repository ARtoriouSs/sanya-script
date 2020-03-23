from parse.AST.values.value import Value


class Node(Value):
    def __init__(self, value, cast = None):
        self.value = value
        super().__init__(cast)
