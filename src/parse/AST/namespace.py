from parse.var import Var
from parse.fun import Fun


class Namespace:
    def __init__(self, parent = None):
        if parent:
            self.vars = parent.vars
            self.funs = parent.funs
        else:
            self.vars = []
            self.funs = []

    def add_var(self, name, type_):
        var = Var(type_, name)
        self._remove_if_exist(var)
        self.vars.append(var)

    def add_fun(self, name, return_type, args):
        fun = Fun(return_type, name, args)
        self._remove_if_exist(fun)
        self.funs.append(fun)

    def find_var(self, name):
        vars_ = [var for i, var in enumerate(self.vars) if var.name == name]
        return vars_[0] if any(vars_) else None

    def find_fun(self, name, return_type=None, args=None):
        funs = [fun for i, fun in enumerate(self.funs) if fun.name == name]
        if return_type:
            funs = [fun for i, fun in enumerate(funs) if fun.return_type == return_type]
        if args is not None:
            funs = [fun for i, fun in enumerate(funs) if self._compare_args(fun, args)]
        return funs[0] if any(funs) else None

    def has_var(self, name):
        return bool(self.find_var(name))

    def has_fun(self, name, return_type=None, args=None):
        return bool(self.find_fun(name, return_type, args))

    def _remove_if_exist(self, targer):
        for var in self.vars:
            if var.name == targer.name:
                self.vars.remove(var)

        for fun in self.funs:
            if fun.name == targer.name:
                self.funs.remove(fun)

    def _compare_args(self, fun, args):
        if not len(fun.args) == len(args): return False
        for i in range(len(args)):
            if args[i].kind() == "id":
                var = self.find_var(args[i].name)
                if var.type != fun.args[i].type: return False
            else:
                if not args[i].kind() == fun.args[i].type: return False
        return True
