class BlockCompiler:
    def __init__(self, target, indent=0):
        self.file = target
        self.indent = indent

    def compile(self, ast):
        for statement in ast.statements:
            self.file.write("    " * self.indent)
            if statement.kind() == "defvar":
                self._compile_defvar(statement)
            elif statement.kind() == "print_stat":
                self._compile_print(statement)
            elif statement.kind() == "println":
                self._compile_println(statement)
            elif statement.kind() == "assignment":
                self._compile_assignment(statement)
            elif statement.kind() == "return_stat":
                self._compile_return_stat(statement)
            elif statement.kind() == "deffun":
                self._compile_deffun(statement)
            elif statement.kind() == "fun_call":
                self._compile_fun_call(statement)
            elif statement.kind() == "if_stat":
                self._compile_if(statement)

    def _compile_defvar(self, statement):
        self.file.write(f"{statement.name} = {statement.type.capitalize()}()\n")

    def _compile_print(self, statement):
        self.file.write(f"{self._resolve_value(statement.value)}.print()\n")

    def _compile_println(self, statement):
        self.file.write(f"{self._resolve_value(statement.value)}.println()\n")

    def _compile_assignment(self, statement):
        self.file.write(f"{statement.target.name} = {self._resolve_value(statement.value)}\n")

    def _compile_return_stat(self, statement):
        self.file.write(f"return {self._resolve_value(statement.value)}\n")

    def _compile_deffun(self, statement):
        self.file.write(f"def {statement.name}({self._resolve_fun_args(statement.args)}):\n")
        self._compile_nested_block(statement.body)

    def _compile_fun_call(self, statement):
        self.file.write(f"{statement.name}({self._resolve_array(statement.args)})\n")

    def _compile_if(self, statement):
        self.file.write(f"if {self._resolve_value(statement.condition)}.cast('logic').value:\n")
        self._compile_nested_block(statement.then)
        if statement.else_ is not None:
            self.file.write(f"else:\n")
            self._compile_nested_block(statement.else_)

    def _resolve_fun_call(self, statement):
        return f"{statement.name}({self._resolve_array(statement.args)})"

    def _resolve_summation(self, statement):
        return f"{self._resolve_value(statement.left)}.summation({self._resolve_value(statement.right)})"

    def _resolve_subtraction(self, statement):
        return f"{self._resolve_value(statement.left)}.subtraction({self._resolve_value(statement.right)})"

    def _resolve_multiplication(self, statement):
        return f"{self._resolve_value(statement.left)}.multiplication({self._resolve_value(statement.right)})"

    def _resolve_division(self, statement):
        return f"{self._resolve_value(statement.left)}.division({self._resolve_value(statement.right)})"

    def _resolve_and(self, statement):
        return f"{self._resolve_value(statement.left)}.and_({self._resolve_value(statement.right)})"

    def _resolve_or(self, statement):
        return f"{self._resolve_value(statement.left)}.or_({self._resolve_value(statement.right)})"

    def _resolve_not(self, statement):
        return f"{self._resolve_value(statement.target)}.not_()"

    def _resolve_equal(self, statement):
        return f"{self._resolve_value(statement.left)}.equal({self._resolve_value(statement.right)})"

    def _resolve_not_equal(self, statement):
        return f"{self._resolve_value(statement.left)}.not_equal({self._resolve_value(statement.right)})"

    def _resolve_greater_or_equal(self, statement):
        return f"{self._resolve_value(statement.left)}.greater_or_equal({self._resolve_value(statement.right)})"

    def _resolve_less_or_equal(self, statement):
        return f"{self._resolve_value(statement.left)}.less_or_equal({self._resolve_value(statement.right)})"

    def _resolve_greater(self, statement):
        return f"{self._resolve_value(statement.left)}.greater({self._resolve_value(statement.right)})"

    def _resolve_less(self, statement):
        return f"{self._resolve_value(statement.left)}.less({self._resolve_value(statement.right)})"

    def _resolve_fun_args(self, args):
        args = [arg.name for arg in args]
        return ", ".join(args)

    def _resolve_value(self, value):
        if value.kind() == "id":
            string = value.name
        elif value.kind() == "node":
            string = f"Node({value.value})"
        elif value.kind() == "arc":
            string = f"Arc({self._resolve_value(value.source)}, {self._resolve_value(value.target)}, {value.weight}, \"{value.type}\")"
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
        return string

    def _resolve_graph_value(self, value):
        return f"Graph([{self._resolve_array(value.elements)}])"

    def _resolve_array(self, values):
        values_ = [self._resolve_value(value) for value in values]
        return ", ".join(values_)

    def _compile_nested_block(self, block):
        if any(block.statements):
            self.__class__(self.file, self.indent + 1).compile(block)
        else:
            self.file.write(f"    pass\n")
