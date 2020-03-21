class Namespace:
    def __init__(self, parent = None):
        if parent:
            self.vars = parent.vars
            self.funs = parent.funs
        else:
            self.vars = []
            self.funs = []

    def add_var(self, var):
        self.vars.append(var)

    def add_fun(self, fun):
        self.funs.append(fun)
