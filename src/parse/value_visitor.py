from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from src.parse.AST.statements.id import Id
from src.runtime.node import Node
import parse.errors as errors


class ValueVisitor(SanyaScriptVisitor):
    def visitNodeValue(self, ctx):
        return Node(int(ctx.INT().getText()))

    def visitArcValue(self, ctx):
        pass

    def visitGraphValue(self, ctx):
        pass

    def visitIdValue(self, ctx):
        return Id(ctx.ID().getText())
