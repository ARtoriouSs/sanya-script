from parser.AST.values.operations.binary_operation import BinaryOperation


class Summation(BinaryOperation):
    def __init__(self, left, right):
        self.operation = "+"
        super().__init__(left, right)
