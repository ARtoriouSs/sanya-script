from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.AST.values.graph import Graph
from parse.AST.values.id import Id
from parse.AST.values.node import Node
from parse.AST.values.arc import Arc
from parse.AST.values.fun_call import FunCall
from parse.parse_error import ParseError
from parse.visitors.function_visitor import FunctionVisitior


class ValueVisitor(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitNodeValue(self, ctx):
        return Node(int(ctx.INT().getText())).cast(self.visitCast(ctx.cast()))

    def visitArcValue(self, ctx):
        source = self.visit(ctx.arcPart(0))
        target = self.visit(ctx.arcPart(1))
        type_, weight = self.visit(ctx.arc())
        return Arc(source, target, weight, type_).cast(self.visitCast(ctx.cast()))

    def visitGraphValue(self, ctx):
        graph = Graph().cast(self.visitCast(ctx.cast()))
        for value in ctx.value():
            val = self.visit(value)
            graph.elements.append(val)
        return graph

    def visitIdValue(self, ctx):
        name = ctx.ID().getText()
        var = self.namespace.find_var(name)
        if var is None: ParseError.undef(name)
        return Id(name, var.type).cast(self.visitCast(ctx.cast()))

    def visitFunCallValue(self, ctx):
        fun_call = self._function_visitor().visit(ctx.funCall())
        fun = self.namespace.find_fun(fun_call.name)
        return FunCall(fun_call, fun.type).cast(self.visitCast(ctx.cast()))

    def visitArcPart(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            var = self.namespace.find_var(name)
            if var is not None:
                return Id(name) if var.type == "node" else ParseError.type_error(var.name, var.type, "node")
            else:
                ParseError.undef(name)
        else:
            return Node(int(ctx.INT().getText()))

    def visitSimpleArc(self, ctx):
        return ["directed", 0]

    def visitSimpleUndirectedArc(self, ctx):
        return ["undirected", 0]

    def visitWeightedArc(self, ctx):
        return ["directed", int(ctx.INT().getText())]

    def visitWeightedUndirectedArc(self, ctx):
        return ["undirected", int(ctx.INT().getText())]

    def visitCast(self, ctx):
        return ctx.type().getText() if ctx else None

    def _function_visitor(self):
        return FunctionVisitior(self.block, self.namespace)
