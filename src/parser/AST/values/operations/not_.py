from parser.AST.values.operations.logical_operation import LogicalOperation


class Not(LogicalOperation):
    def __init__(self, target):
        self.operation = "not"
        super().__init__(target)
