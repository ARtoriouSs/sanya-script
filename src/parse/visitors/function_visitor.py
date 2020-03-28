from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.AST.fun_arg import FunArg
from parse.AST.statements.deffun import Deffun
from parse.AST.statements.fun_call import FunCall
from parse.parse_error import ParseError


class FunctionVisitior(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitDeffun(self, ctx):
        return_type = ctx.type().getText() if ctx.type() else None
        name = ctx.ID().getText()
        args = self.visit(ctx.funArg()) if ctx.funArg() else []
        body = self.visit(ctx.block())
        self.namespace.add_fun(name, return_type, args)
        return Deffun(name, args, body)

    def visitFunArg(self, ctx):
        value = FunArg(ctx.type().getText(), ctx.ID().getText())
        rest = self.visit(ctx.funArg()) if ctx.funArg() else []
        return [value] + rest

    def visitBlock(self, ctx):
        from parse.visitors.visitor import Visitor
        return Visitor().visitSanyaScript(ctx)

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
        from parse.visitors.value_visitor import ValueVisitor
        return ValueVisitor(self.block, self.namespace)

    def _arg_types(self, args):
        types = []
        for arg in args:
            if arg.kind() == "id":
                types.append(str(self.namespace.find_var(arg.name).type))
            else:
                types.append(str(arg.kind()))
        return types
