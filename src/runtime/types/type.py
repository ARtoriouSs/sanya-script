class Type:
    def print(self):
        pass

    def println(self):
        self.print()
        print()

    def cast(self, type_):
        pass

    def summation(self, value):
        pass

    def subtraction(self, value):
        pass

    def multiplication(self, value):
        pass

    def division(self, value):
        pass

    def and_(self, value):
        from .logic import Logic
        return Logic(self.cast("logic").value and value.cast("logic").value)

    def or_(self, value):
        from .logic import Logic
        return Logic(self.cast("logic").value or value.cast("logic").value)

    def not_(self):
        from .logic import Logic
        return Logic(not self.cast("logic").value)

    def equal(self, value):
        from .logic import Logic
        return Logic(self.value == value.value)

    def not_equal(self, value):
        from .logic import Logic
        return Logic(self.value != value.value)

    def greater_or_equal(self, value):
        pass

    def less_or_equal(self, value):
        pass

    def greater(self, value):
        pass

    def less(self, value):
        pass
