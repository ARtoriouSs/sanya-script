from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor

from src.parse.AST.values.graph import Graph
from src.parse.AST.values.id import Id
from src.parse.AST.values.node import Node
from src.parse.AST.values.arc import Arc
import parse.errors as errors


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
            if val.kind() == "node": graph.nodes.append(val)
            if val.kind() == "arc": graph.arcs.append(val)
            if val.kind() == "graph": graph.merge(val)
        return graph

    def visitIdValue(self, ctx):
        return Id(ctx.ID().getText()).cast(self.visitCast(ctx.cast()))

    def visitArcPart(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            var = self.namespace.find_var(name)
            if var:
                return Id(name) if var.type == "node" else errors.type_error(var.name, var.type, "node")
            else:
                errors.undef(name)
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

