from parser.AST.values.value import Value
from parser.parse_error import ParseError


class BinaryOperation(Value):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        super().__init__()

    def kind(self):
        return "binary_operation." + super().kind()

    def return_type(self):
        if self.cast_type is not None: return self.cast_type

        if self.left.return_type() == "num" and self.right.return_type() == "num":
            return "num"
        elif self.left.return_type() == "arc" and self.right.return_type() == "num":
            return "arc"
        elif self.left.return_type() == "node" and self.right.return_type() == "num":
            return "node"
        elif self.left.return_type() == "graph" and self.right.return_type() == "graph":
            return "graph"
        else:
            ParseError.incompatible_operation(super().kind(), self.left.return_type(), self.right.return_type())
