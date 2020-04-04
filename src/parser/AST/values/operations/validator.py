class Validator:
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right

    def is_valid(self):
        if self.right.return_type() == "graph" and self.left.return_type() == "graph":
            return True
        elif self.left.return_type() in ["node", "arc", "num"] and self.right.return_type() == "num":
            return True
        else:
            return False
