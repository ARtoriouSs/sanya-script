import re

from parser.compilation_error import CompilationError
from analyzer.operations_validator import OperationsValidator
from analyzer.cast_validator import CastValidator


class ValueAnalyzer:
    def __init__(self, error):
        self.error = error

    def validate(self, value):
        if value.kind() == "id":
            self._check_id_value(value)
        elif value.kind() == "node":
            self._check_node_value(value)
        elif value.kind() == "arc":
            self._check_arc_value(value)
        elif value.kind() == "graph":
            self._check_graph_value(value)
        elif value.kind() == "fun_call":
            self._check_fun_call_value(value)
        elif value.kind() == "unary_operation.not":
            self._check_not_value(value)
        elif re.match(r"binary_operation\..*", value.kind()):
            self._check_binary_operation_value(value)

        if value.cast_type is not None: self._check_cast_type(value)
        if value.index is not None: self._check_index(value)

        return True

    def _check_id_value(self, value):
        if value.var.undef: self.error.undef(value.name)

    def _check_arc_value(self, value):
        source = value.source
        target = value.target
        weight = value.weight

        self.validate(source)
        self.validate(target)
        self.validate(weight)

        if source.return_type() != "node": self.error.arc_error(source.return_type())
        if target.return_type() != "node": self.error.arc_error(target.return_type())
        if weight.return_type() != "num": self.error.arc_weight_error(weight.return_type())

    def _check_not_value(self, value):
        self.validate(value.target)

        if not OperationsValidator("not", target=value.target).is_valid():
            self.error.incompatible_unary_operation("not", value.target.return_type())

    def _check_binary_operation_value(self, value):
        operation = value.operation
        left = value.left
        right = value.right

        self.validate(left)
        self.validate(right)

        if not OperationsValidator(operation, left, right).is_valid():
            self.error.incompatible_operation(operation, left.return_type(), right.return_type())

    def _check_fun_call_value(self, value):
        for arg in value.fun_call.args:
            self.validate(arg)

    def _check_graph_value(self, value):
        for element in value.elements:
            self.validate(element)
            if element.return_type() not in ["node", "arc", "graph"]:
                self.error.graph_value_error(element.return_type())

    def _check_node_value(self, value):
        self.validate(value.value)
        if value.value.return_type() != "num":
            self.error.node_value_error(value.value.return_type())

    def _check_cast_type(self, value):
        if not CastValidator(value).is_valid():
            self.error.cast_error(value.kind(), value.cast_type)

    def _check_index(self, value):
        if not re.match(r".*{}", value.ret_type):
            self.error.cannot_be_indexed(value.ret_type)
        if value.index.return_type() != "num":
            self.error.incorrect_index_type(value.index.return_type())
