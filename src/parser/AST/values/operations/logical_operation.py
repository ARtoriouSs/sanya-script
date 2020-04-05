from parser.AST.values.operations.binary_operation import BinaryOperation


class LogicalOperation(BinaryOperation):
    def return_type(self):
        return self.cast_type if self.cast_type is not None else "logic"
