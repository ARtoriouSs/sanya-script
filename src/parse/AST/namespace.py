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

    def has(self, name):
        return self.has_var(name) | self.has_fun(name)

    def has_var(self, name):
        return True if any(var.name == name for var in self.vars) else False

    def has_fun(self, name):
        return True if any(var.name == name for var in self.vars) else False
