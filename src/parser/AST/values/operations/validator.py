class Validator:
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right

    def is_valid(self):
        if self.operation == "*":
            return self.validate_multiplication()
        elif self.operation == "/":
            return self.validate_division()
        elif self.operation == "+":
            return self.validate_summation()
        elif self.operation == "-":
            return self.validate_subtraction()

    def validate_multiplication(self):
        if self.right.return_type() == "graph" and self.left.return_type() == "graph":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False

    def validate_division(self):
        if self.right.return_type() == "graph" and self.left.return_type() == "graph":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False

    def validate_summation(self):
        if self.right.return_type() == "graph" and self.left.return_type() != "num":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False

    def validate_subtraction(self):
        if self.right.return_type() == "graph" and self.left.return_type() != "num":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False
