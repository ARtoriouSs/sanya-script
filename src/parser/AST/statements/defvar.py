import re

from parser.AST.statements.statement import Statement


class Defvar(Statement):
    def __init__(self, var):
        self.type = var.type
        self.name = var.name
        self.is_const = var.is_const
        self.undef = False

    def is_array(self):
        return True if re.match(r".*{}", self.type) else False
