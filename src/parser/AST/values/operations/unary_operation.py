from parser.AST.values.value import Value


class UnaryOperation(Value):
    def __init__(self, target):
        self.target = target
        super().__init__()

    def kind(self):
        return "unary_operation." + super().kind()

    def return_type(self):
        return self.cast_type if self.cast_type is not None else "logic"
