from parser.AST.values.operations.logical_operation import LogicalOperation


class And(LogicalOperation):
    def __init__(self, left, right):
        self.operation = "and"
        super().__init__(left, right)
