from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from src.parse.AST.id import Id
from src.parse.AST.values.node import Node
from src.parse.AST.values.arc import Arc
import parse.errors as errors


class ValueVisitor(SanyaScriptVisitor):
    def visitNodeValue(self, ctx):
        return Node(int(ctx.INT().getText()))

    def visitArcValue(self, ctx):
        source = self.visit(ctx.arcPart(0))
        target = self.visit(ctx.arcPart(1))
        type_, weight = self.visit(ctx.arc())
        return Arc(source, target, weight, type_)

    def visitGraphValue(self, ctx):
        pass

    def visitIdValue(self, ctx):
        return Id(ctx.ID().getText())

    def visitArcPart(self, ctx):
        return Id(ctx.ID().getText()) if ctx.ID() else Node(int(ctx.INT().getText()))

    def visitSimpleArc(self, ctx):
        return ["directed", 0]

    def visitSimpleUndirectedArc(self, ctx):
        return ["undirected", 0]

    def visitWeightedArc(self, ctx):
        return ["directed", int(ctx.INT().getText())]

    def VisitWeightedUndirectedArc(self, ctx):
        return ["undirected", int(ctx.INT().getText())]
