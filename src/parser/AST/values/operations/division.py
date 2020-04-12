from parser.AST.values.operations.binary_operation import BinaryOperation


class Division(BinaryOperation):
    def __init__(self, left, right):
        self.operation = "/"
        super().__init__(left, right)
