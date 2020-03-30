from parser.AST.values.value import Value


class BinaryOperation(Value):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        super().__init__()

    def kind(self):
        return "binary_operation." + super().kind()
