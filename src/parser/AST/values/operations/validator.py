class Validator:
    def __init__(self, operation, left=None, right=None, target=None):
        self.operation = operation
        self.left = left
        self.right = right
        self.target = target

    def is_valid(self):
        if self.operation in ["+", "-", "*", "/"]:
            self.validate_arithmetic()
        elif self.operation in ["and", "or", "not", "==", "!=", ">=", "<=", ">", "<"]:
            self.validate_logical()

    def validate_arithmetic(self):
        if self.right.return_type() == "graph" and self.left.return_type() == "graph":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False

    def validate_logical(self):
        return True
