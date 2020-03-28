from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.parse_error import ParseError
from parser.AST.fun_arg import FunArg
from parser.AST.statements.deffun import Deffun
from parser.AST.statements.fun_call import FunCall


class FunctionVisitior(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitDeffun(self, ctx):
        return_type = ctx.type_().getText() if ctx.type_() else None
        name = ctx.ID().getText()
        args = self.visit(ctx.funArg()) if ctx.funArg() else []
        body = self.visit(ctx.block())
        self.namespace.add_fun(name, return_type, args)
        return Deffun(name, args, body)

    def visitFunArg(self, ctx):
        value = FunArg(ctx.type_().getText(), ctx.ID().getText())
        rest = self.visit(ctx.funArg()) if ctx.funArg() else []
        return [value] + rest

    def visitBlock(self, ctx):
        return self._visitor().visitSanyaScript(ctx)

    def visitFunCall(self, ctx):
        name = ctx.ID().getText()
        args = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        fun = self.namespace.find_fun(name, args=args)
        if fun is None: ParseError.signature_not_found(name, self._arg_types(args))
        return FunCall(name, fun.return_type, args)

    def visitParamValue(self, ctx):
        value = self._value_visitor().visit(ctx.value())
        rest = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        return [value] + rest

    def _value_visitor(self):
        from parse.visitors.value_visitor import ValueVisitor
        return ValueVisitor(self.block, self.namespace)

    def _visitor(self):
        from parse.visitors.visitor import Visitor
        return Visitor(self.block, self.namespace)

    def _arg_types(self, args):
        return [arg.return_type() for arg in args]
