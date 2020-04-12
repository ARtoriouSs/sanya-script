from parser.var import Var
from parser.fun import Fun


class Namespace:
    def __init__(self, parent=None):
        self.vars = []
        self.funs = []
        if parent: self.merge(parent)

    def merge(self, namespace):
        self.vars += namespace.vars
        self.funs += namespace.funs

    def add_var(self, name, type_, is_const=False):
        var = Var(type_, name, is_const)
        self._remove_var_if_exist(var)
        self.vars.append(var)
        return var

    def add_fun(self, name, return_type, args):
        fun = Fun(return_type, name, args)
        self._remove_fun_if_exist(fun)
        self.funs.append(fun)
        return fun

    def find_var(self, name):
        vars_ = [var for var in self.vars if var.name == name]
        return vars_[0] if any(vars_) else Var('nope', name, undef=True)

    def find_fun(self, name, return_type=None, args=None):
        funs = [fun for fun in self.funs if fun.name == name]
        if return_type is not None:
            funs = [fun for fun in funs if fun.return_type == return_type]
        if args is not None:
            funs = [fun for fun in funs if self._compare_args(fun, args)]
        return funs[0] if any(funs) else Fun(name, return_type, args, undef=True)

    def has_var(self, name):
        return bool(self.find_var(name))

    def has_fun(self, name, return_type=None, args=None):
        return bool(self.find_fun(name, return_type, args))

    def _remove_var_if_exist(self, target):
        for var in self.vars:
            if var.name == target.name:
                self.vars.remove(var)

    def _remove_fun_if_exist(self, target):
        for fun in self.funs:
            if fun.name == target.name and fun.return_type == target.return_type and self._compare_fun_args(fun, target):
                self.funs.remove(fun)

    def _compare_fun_args(self, first, second):
        if not len(first.args) == len(second.args): return False
        for i, arg in enumerate(first.args):
            if not arg.type == second.args[i].type: return False
        return True

    def _compare_args(self, fun, args):
        if not len(fun.args) == len(args): return False
        for i, arg in enumerate(args):
            if not arg.return_type() == fun.args[i].type: return False
        return True
