from parser.AST.values.operations.logical_operation import LogicalOperation


class Equal(LogicalOperation):
    def __init__(self, left, right):
        self.operation = "=="
        super().__init__(left, right)
