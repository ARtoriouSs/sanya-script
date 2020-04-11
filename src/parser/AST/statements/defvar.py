import re

from parser.AST.statements.statement import Statement


class Defvar(Statement):
    def __init__(self, type_, name, is_const=False):
        self.type = type_
        self.name = name
        self.is_const = is_const

    def is_array(self):
        return True if re.match(r".*{}", self.type) else False
