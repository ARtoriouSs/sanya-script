from parse.AST.namespace import Namespace


class Block:
    def __init__(self, namespace = None):
        self.namespace = namespace or Namespace()
        self.statements = []

    def add_statement(self, statement):
        self.statements.append(statement)

    def add_local_var(self, local):
        self.namespace.add_var(local)

    def add_local_fun(self, local):
        self.namespace.add_fun(local)
