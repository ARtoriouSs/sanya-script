import copy

from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.AST.values.nope import Nope
from parser.AST.fun_arg import FunArg
from parser.AST.statements.deffun import Deffun
from parser.AST.statements.fun_call import FunCall


class FunctionVisitior(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = copy.copy(namespace)
        self.block = block

    def visitDeffun(self, ctx):
        return_type = ctx.type_().getText() if ctx.type_() else "nope"
        name = ctx.ID().getText()
        args = self.visit(ctx.funArg()) if ctx.funArg() else []
        body = self._visitor(args).visitSanyaScript(ctx.block())
        self.namespace.add_fun(name, return_type, args)
        return Deffun(return_type, name, args, body)

    def visitFunArg(self, ctx):
        value = FunArg(ctx.type_().getText(), ctx.ID().getText())
        rest = self.visit(ctx.funArg()) if ctx.funArg() else []
        return [value] + rest

    def visitFunCall(self, ctx):
        name = ctx.ID().getText()
        args = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        fun = self.namespace.find_fun(name, args=args)
        return FunCall(fun, args)

    def visitParamValue(self, ctx):
        value = self._value_visitor().visit(ctx.value())
        rest = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        return [value] + rest

    def _value_visitor(self):
        from parser.visitors.value_visitor import ValueVisitor
        return ValueVisitor(self.block, self.namespace)

    def _visitor(self, locals_=()):
        from parser.visitors.visitor import Visitor
        return Visitor(self.namespace, locals_)
