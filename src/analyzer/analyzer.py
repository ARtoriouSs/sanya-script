class Analyzer:
    def __init__(self, ast):
        self.ast = ast

    def validate(self):
        for statement in self.ast.statements:
            self._check(statement)
        return True

    def _check(self, statement):
        pass
