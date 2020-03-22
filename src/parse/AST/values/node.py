from parse.AST.values.value import Value


class Node(Value):
    def __init__(self, value):
        self.value = value
