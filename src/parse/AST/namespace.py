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

    def find_var(self, name):
        vars_ = [var for i, var in enumerate(self.vars) if var.name == name]
        return vars_[0] if any(vars_) else None

    def find_fun(self, name):
        funs = [fun for i, fun in enumerate(self.funs) if fun.name == name]
        return funs[0] if any(funs) else None

    def has_var(self, name):
        return any([var for var in self.vars if var.name == name])

    def has_fun(self, name):
        return any([fun for fun in self.funs if fun.name == name])
