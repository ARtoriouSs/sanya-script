# Generated from src/grammar/SanyaScript.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SanyaScriptParser import SanyaScriptParser
else:
    from SanyaScriptParser import SanyaScriptParser

# This class defines a complete listener for a parse tree produced by SanyaScriptParser.
class SanyaScriptListener(ParseTreeListener):

    # Enter a parse tree produced by SanyaScriptParser#sanyaScript.
    def enterSanyaScript(self, ctx:SanyaScriptParser.SanyaScriptContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#sanyaScript.
    def exitSanyaScript(self, ctx:SanyaScriptParser.SanyaScriptContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#assignment.
    def enterAssignment(self, ctx:SanyaScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#assignment.
    def exitAssignment(self, ctx:SanyaScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#defvar.
    def enterDefvar(self, ctx:SanyaScriptParser.DefvarContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#defvar.
    def exitDefvar(self, ctx:SanyaScriptParser.DefvarContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#defnode.
    def enterDefnode(self, ctx:SanyaScriptParser.DefnodeContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#defnode.
    def exitDefnode(self, ctx:SanyaScriptParser.DefnodeContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#defarc.
    def enterDefarc(self, ctx:SanyaScriptParser.DefarcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#defarc.
    def exitDefarc(self, ctx:SanyaScriptParser.DefarcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#defgraph.
    def enterDefgraph(self, ctx:SanyaScriptParser.DefgraphContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#defgraph.
    def exitDefgraph(self, ctx:SanyaScriptParser.DefgraphContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#arc.
    def enterArc(self, ctx:SanyaScriptParser.ArcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#arc.
    def exitArc(self, ctx:SanyaScriptParser.ArcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#simpleArc.
    def enterSimpleArc(self, ctx:SanyaScriptParser.SimpleArcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#simpleArc.
    def exitSimpleArc(self, ctx:SanyaScriptParser.SimpleArcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#simpleUndirectedArc.
    def enterSimpleUndirectedArc(self, ctx:SanyaScriptParser.SimpleUndirectedArcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#simpleUndirectedArc.
    def exitSimpleUndirectedArc(self, ctx:SanyaScriptParser.SimpleUndirectedArcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#weightedArc.
    def enterWeightedArc(self, ctx:SanyaScriptParser.WeightedArcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#weightedArc.
    def exitWeightedArc(self, ctx:SanyaScriptParser.WeightedArcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#weightedUndirectedArc.
    def enterWeightedUndirectedArc(self, ctx:SanyaScriptParser.WeightedUndirectedArcContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#weightedUndirectedArc.
    def exitWeightedUndirectedArc(self, ctx:SanyaScriptParser.WeightedUndirectedArcContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#value.
    def enterValue(self, ctx:SanyaScriptParser.ValueContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#value.
    def exitValue(self, ctx:SanyaScriptParser.ValueContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#nodeValue.
    def enterNodeValue(self, ctx:SanyaScriptParser.NodeValueContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#nodeValue.
    def exitNodeValue(self, ctx:SanyaScriptParser.NodeValueContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#arcValue.
    def enterArcValue(self, ctx:SanyaScriptParser.ArcValueContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#arcValue.
    def exitArcValue(self, ctx:SanyaScriptParser.ArcValueContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#graphValue.
    def enterGraphValue(self, ctx:SanyaScriptParser.GraphValueContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#graphValue.
    def exitGraphValue(self, ctx:SanyaScriptParser.GraphValueContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#type.
    def enterType(self, ctx:SanyaScriptParser.TypeContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#type.
    def exitType(self, ctx:SanyaScriptParser.TypeContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#cast.
    def enterCast(self, ctx:SanyaScriptParser.CastContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#cast.
    def exitCast(self, ctx:SanyaScriptParser.CastContext):
        pass


    # Enter a parse tree produced by SanyaScriptParser#print.
    def enterPrint(self, ctx:SanyaScriptParser.PrintContext):
        pass

    # Exit a parse tree produced by SanyaScriptParser#print.
    def exitPrint(self, ctx:SanyaScriptParser.PrintContext):
        pass


