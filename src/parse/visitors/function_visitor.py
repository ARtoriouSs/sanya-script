from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.AST.fun_arg import FunArg
from parse.AST.statements.deffun import Deffun
from parse.AST.statements.fun_call import FunCall
from parse.parse_error import ParseError
from parse.visitors.value_visitor import ValueVisitor


class FunctionVisitior(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitDeffun(self, ctx):
        return_type = ctx.type().getText() if ctx.type() else None
        name = ctx.ID().getText()
        args = self.visit(ctx.funArg()) if ctx.funArg() else []
        body = self.visit(ctx.funBody())
        self.namespace.add_fun(name, return_type, args)
        return Deffun(return_type, name, args, body)

    def visitFunArg(self, ctx):
        value = FunArg(ctx.type().getText(), ctx.ID().getText())
        rest = self.visit(ctx.funArg()) if ctx.funArg() else []
        return [value] + rest

    def visitFunBody(self, ctx):
        from parse.parser import Parser

        start = ctx.start.start
        stop = ctx.stop.stop
        code = ctx.start.getInputStream().getText(start, stop)
        return Parser.parse(code=code)

    def visitFunCall(self, ctx):
        name = ctx.ID().getText()
        args = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        if not self.namespace.has_fun(name, args=args): ParseError.signature_not_found(name, self._arg_types(args))
        return FunCall(name, args)

    def visitParamValue(self, ctx):
        value = self._value_visitor().visit(ctx.value())
        rest = self.visit(ctx.paramValue()) if ctx.paramValue() else []
        return [value] + rest

    def _value_visitor(self):
        return ValueVisitor(self.block, self.namespace)

    def _arg_types(self, args):
        types = []
        for arg in args:
            if arg.kind() == "id":
                types.append(str(self.namespace.find_var(arg.name).type))
            else:
                types.append(str(arg.kind()))
        return types
