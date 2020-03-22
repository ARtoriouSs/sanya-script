# Generated from src/parse/grammar/SanyaScript.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SanyaScriptParser import SanyaScriptParser
else:
    from SanyaScriptParser import SanyaScriptParser

# This class defines a complete generic visitor for a parse tree produced by SanyaScriptParser.

class SanyaScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SanyaScriptParser#sanyaScript.
    def visitSanyaScript(self, ctx:SanyaScriptParser.SanyaScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#statement.
    def visitStatement(self, ctx:SanyaScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#assign.
    def visitAssign(self, ctx:SanyaScriptParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#reassign.
    def visitReassign(self, ctx:SanyaScriptParser.ReassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#cast.
    def visitCast(self, ctx:SanyaScriptParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#defnode.
    def visitDefnode(self, ctx:SanyaScriptParser.DefnodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#defarc.
    def visitDefarc(self, ctx:SanyaScriptParser.DefarcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#defgraph.
    def visitDefgraph(self, ctx:SanyaScriptParser.DefgraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#simpleArc.
    def visitSimpleArc(self, ctx:SanyaScriptParser.SimpleArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#simpleUndirectedArc.
    def visitSimpleUndirectedArc(self, ctx:SanyaScriptParser.SimpleUndirectedArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#weightedArc.
    def visitWeightedArc(self, ctx:SanyaScriptParser.WeightedArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#weightedUndirectedArc.
    def visitWeightedUndirectedArc(self, ctx:SanyaScriptParser.WeightedUndirectedArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#nodeValue.
    def visitNodeValue(self, ctx:SanyaScriptParser.NodeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#arcValue.
    def visitArcValue(self, ctx:SanyaScriptParser.ArcValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#graphValue.
    def visitGraphValue(self, ctx:SanyaScriptParser.GraphValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#idValue.
    def visitIdValue(self, ctx:SanyaScriptParser.IdValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#type.
    def visitType(self, ctx:SanyaScriptParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SanyaScriptParser#print.
    def visitPrint(self, ctx:SanyaScriptParser.PrintContext):
        return self.visitChildren(ctx)



del SanyaScriptParser