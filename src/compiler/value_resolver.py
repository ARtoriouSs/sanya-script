class ValueResolver:
    def resolve(self, value):
        if value.kind() == "id":
            string = self._resolve_id_value(value)
        elif value.kind() == "node":
            string = f"Node({self.resolve(value.value)}.value)"
        elif value.kind() == "arc":
            string = f"Arc({self.resolve(value.source)}, {self.resolve(value.target)}, {self.resolve(value.weight)}.value, \"{value.type}\")"
        elif value.kind() == "graph":
            string = self._resolve_graph_value(value)
        elif value.kind() == "num":
            string = f"Num({value.value})"
        elif value.kind() == "logic":
            string = f"Logic({value.value})"
        elif value.kind() == "nope":
            string = "Nope()"
        elif value.kind() == "fun_call":
            string = self._resolve_fun_call(value.fun_call)
        elif value.kind() == "binary_operation.summation":
            string = self._resolve_summation(value)
        elif value.kind() == "binary_operation.subtraction":
            string = self._resolve_subtraction(value)
        elif value.kind() == "binary_operation.multiplication":
            string = self._resolve_multiplication(value)
        elif value.kind() == "binary_operation.division":
            string = self._resolve_division(value)
        elif value.kind() == "binary_operation.and":
            string = self._resolve_and(value)
        elif value.kind() == "binary_operation.or":
            string = self._resolve_or(value)
        elif value.kind() == "unary_operation.not":
            string = self._resolve_not(value)
        elif value.kind() == "binary_operation.equal":
            string = self._resolve_equal(value)
        elif value.kind() == "binary_operation.not_equal":
            string = self._resolve_not_equal(value)
        elif value.kind() == "binary_operation.greater_or_equal":
            string = self._resolve_greater_or_equal(value)
        elif value.kind() == "binary_operation.less_or_equal":
            string = self._resolve_less_or_equal(value)
        elif value.kind() == "binary_operation.greater":
            string = self._resolve_greater(value)
        elif value.kind() == "binary_operation.less":
            string = self._resolve_less(value)

        string += f".cast(\"{value.cast_type}\")" if value.cast_type else ""
        string += f"[{int(value.index.value)}]" if value.index else ""
        return string


    def _resolve_fun_call(self, statement):
        return f"{statement.name}({self._resolve_array(statement.args)})"

    def _resolve_summation(self, statement):
        return f"{self.resolve(statement.left)}.summation({self.resolve(statement.right)})"

    def _resolve_subtraction(self, statement):
        return f"{self.resolve(statement.left)}.subtraction({self.resolve(statement.right)})"

    def _resolve_multiplication(self, statement):
        return f"{self.resolve(statement.left)}.multiplication({self.resolve(statement.right)})"

    def _resolve_division(self, statement):
        return f"{self.resolve(statement.left)}.division({self.resolve(statement.right)})"

    def _resolve_and(self, statement):
        return f"{self.resolve(statement.left)}.and_({self.resolve(statement.right)})"

    def _resolve_or(self, statement):
        return f"{self.resolve(statement.left)}.or_({self.resolve(statement.right)})"

    def _resolve_not(self, statement):
        return f"{self.resolve(statement.target)}.not_()"

    def _resolve_equal(self, statement):
        return f"{self.resolve(statement.left)}.equal({self.resolve(statement.right)})"

    def _resolve_not_equal(self, statement):
        return f"{self.resolve(statement.left)}.not_equal({self.resolve(statement.right)})"

    def _resolve_greater_or_equal(self, statement):
        return f"{self.resolve(statement.left)}.greater_or_equal({self.resolve(statement.right)})"

    def _resolve_less_or_equal(self, statement):
        return f"{self.resolve(statement.left)}.less_or_equal({self.resolve(statement.right)})"

    def _resolve_greater(self, statement):
        return f"{self.resolve(statement.left)}.greater({self.resolve(statement.right)})"

    def _resolve_less(self, statement):
        return f"{self.resolve(statement.left)}.less({self.resolve(statement.right)})"

    def _resolve_id_value(self, statement):
        if statement.index is not None:
            return statement.name + f"[int({self.resolve(statement.index)}.value)]"
        else:
            return statement.name

    def _resolve_graph_value(self, value):
        return f"Graph([{self._resolve_array(value.elements)}])"

    def _resolve_array(self, values):
        values_ = [self.resolve(value) for value in values]
        return ", ".join(values_)
