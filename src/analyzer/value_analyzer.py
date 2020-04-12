import re

from parser.parse_error import ParseError
from analyzer.operations_validator import OperationsValidator


class ValueAnalyzer:
    def __init__(self, error):
        self.error = error

    def validate(self, value):
        if value.kind() == "id":
            self._check_id_value(value)
        elif value.kind() == "arc":
            self._check_arc_value(value)
        elif value.kind() == "unary_operation.not":
            self._check_not_value(value)
        elif re.match(r"binary_operation\..*", value.kind()):
            self._check_binary_operation_value(value)

        if value.cast is not None: self._check_cast_type(value)
        if value.index is not None: self._check_index(value)

        return True

    def _check_id_value(self, value):
        if value.var.undef: ParseError.undef(value.name)

    def _check_arc_value(self, value):
        if value.source.return_type() != "node": ParseError.arc_error(value.source.return_type())
        if value.target.return_type() != "node": ParseError.arc_error(value.target.return_type())

    def _check_not_value(self, value):
        if not OperationsValidator("not", target=value.target).is_valid():
            ParseError.incompatible_unary_operation("not", value.target.return_type())

    def _check_binary_operation_value(self, value):
        operation = value.operation
        left = value.left
        right = value.right
        if not OperationsValidator(operation, left, right).is_valid():
            ParseError.incompatible_operation(operation, left.return_type(), right.return_type())

    def _check_cast_type(self, value):
        pass

    def _check_index(self, value):
        if not re.match(r".*{}", value.ret_type):
            ParseError.cannot_be_indexed(value.ret_type)
        if value.index.return_type() != "num":
            ParseError.incorrect_index_type(value.index.return_type())
