from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.parser import Parser
from parse.AST.fun_arg import FunArg


class FunctionVisitior(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitDeffun(self, ctx):
        return_type = ctx.type().getText() if ctx.type() else None
        name = ctx.ID().getText()
        args = self.visit(ctx.funArg()) if ctx.funArg() else []
        body = Parser.parse(code=ctx.funBody().getText())
        return Deffun(return_type, name, args, body)

    def visitFunArg(self, ctx):
        value = FunArg(ctx.type().getText(), ctx.ID().getText())
        rest = self.visit(ctx.funArg()) if ctx.funArg() else []
        return [value] + rest
