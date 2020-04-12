from parser.AST.values.operations.logical_operation import LogicalOperation


class Or(LogicalOperation):
    def __init__(self, left, right):
        self.operation = "or"
        super().__init__(left, right)
