# Generated from src/grammar/SanyaScript.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\5\4%\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4,\n\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7E\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\7\bP\n\b\f\b\16\bS\13\b\3\b\3\b\3\b\3\b\5\bY\n\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\4")
        buf.write("\3\2\26\27\3\2\n\f\2e\2\27\3\2\2\2\4\37\3\2\2\2\6.\3\2")
        buf.write("\2\2\b\60\3\2\2\2\n:\3\2\2\2\fD\3\2\2\2\16X\3\2\2\2\20")
        buf.write("Z\3\2\2\2\22\\\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26")
        buf.write("\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2")
        buf.write("\31\27\3\2\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34 \5\n\6\2")
        buf.write("\35 \5\6\4\2\36 \5\22\n\2\37\34\3\2\2\2\37\35\3\2\2\2")
        buf.write("\37\36\3\2\2\2 \5\3\2\2\2!\"\5\n\6\2\"$\7\21\2\2#%\5\b")
        buf.write("\5\2$#\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\5\16\b\2\'/\3\2")
        buf.write("\2\2()\7\27\2\2)+\7\21\2\2*,\5\b\5\2+*\3\2\2\2+,\3\2\2")
        buf.write("\2,-\3\2\2\2-/\5\16\b\2.!\3\2\2\2.(\3\2\2\2/\7\3\2\2\2")
        buf.write("\60\61\7\3\2\2\61\62\5\20\t\2\62\63\7\4\2\2\63\t\3\2\2")
        buf.write("\2\64\65\7\n\2\2\65;\7\27\2\2\66\67\7\13\2\2\67;\7\27")
        buf.write("\2\289\7\f\2\29;\7\27\2\2:\64\3\2\2\2:\66\3\2\2\2:8\3")
        buf.write("\2\2\2;\13\3\2\2\2<E\7\5\2\2=E\7\6\2\2>?\7\r\2\2?@\7\26")
        buf.write("\2\2@E\7\17\2\2AB\7\16\2\2BC\7\26\2\2CE\7\17\2\2D<\3\2")
        buf.write("\2\2D=\3\2\2\2D>\3\2\2\2DA\3\2\2\2E\r\3\2\2\2FY\7\26\2")
        buf.write("\2GH\t\2\2\2HI\5\f\7\2IJ\t\2\2\2JY\3\2\2\2KQ\7\7\2\2L")
        buf.write("M\5\16\b\2MN\7\b\2\2NP\3\2\2\2OL\3\2\2\2PS\3\2\2\2QO\3")
        buf.write("\2\2\2QR\3\2\2\2RT\3\2\2\2SQ\3\2\2\2TU\5\16\b\2UV\7\t")
        buf.write("\2\2VY\3\2\2\2WY\7\27\2\2XF\3\2\2\2XG\3\2\2\2XK\3\2\2")
        buf.write("\2XW\3\2\2\2Y\17\3\2\2\2Z[\t\3\2\2[\21\3\2\2\2\\]\7\20")
        buf.write("\2\2]^\7\27\2\2^\23\3\2\2\2\13\27\37$+.:DQX")
        return buf.getvalue()


class SanyaScriptParser ( Parser ):

    grammarFileName = "SanyaScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'->'", "'<->'", "'['", 
                     "','", "']'", "'node'", "'arc'", "'graph'", "'-['", 
                     "'<-['", "']->'", "'print'", "'='", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NODE_TYPE", "ARC_TYPE", "GRAPH_TYPE", "WEIGHTED_ARC_START", 
                      "WEIGHTED_UNDIRECTED_ARC_START", "WEIGHTED_ARC_END", 
                      "PRINT", "EQUALS", "PLUS", "MINUS", "MULT", "DIV", 
                      "INT", "ID", "WS", "COMMENT" ]

    RULE_sanyaScript = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_cast = 3
    RULE_defvar = 4
    RULE_arc = 5
    RULE_value = 6
    RULE_type = 7
    RULE_print = 8

    ruleNames =  [ "sanyaScript", "statement", "assignment", "cast", "defvar", 
                   "arc", "value", "type", "print" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NODE_TYPE=8
    ARC_TYPE=9
    GRAPH_TYPE=10
    WEIGHTED_ARC_START=11
    WEIGHTED_UNDIRECTED_ARC_START=12
    WEIGHTED_ARC_END=13
    PRINT=14
    EQUALS=15
    PLUS=16
    MINUS=17
    MULT=18
    DIV=19
    INT=20
    ID=21
    WS=22
    COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SanyaScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SanyaScriptParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SanyaScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(SanyaScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_sanyaScript

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSanyaScript" ):
                return visitor.visitSanyaScript(self)
            else:
                return visitor.visitChildren(self)




    def sanyaScript(self):

        localctx = SanyaScriptParser.SanyaScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sanyaScript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SanyaScriptParser.NODE_TYPE) | (1 << SanyaScriptParser.ARC_TYPE) | (1 << SanyaScriptParser.GRAPH_TYPE) | (1 << SanyaScriptParser.PRINT) | (1 << SanyaScriptParser.ID))) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(SanyaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defvar(self):
            return self.getTypedRuleContext(SanyaScriptParser.DefvarContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SanyaScriptParser.AssignmentContext,0)


        def print(self):
            return self.getTypedRuleContext(SanyaScriptParser.PrintContext,0)


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SanyaScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.defvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.print()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defvar(self):
            return self.getTypedRuleContext(SanyaScriptParser.DefvarContext,0)


        def EQUALS(self):
            return self.getToken(SanyaScriptParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(SanyaScriptParser.ValueContext,0)


        def cast(self):
            return self.getTypedRuleContext(SanyaScriptParser.CastContext,0)


        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def getRuleIndex(self):
            return SanyaScriptParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SanyaScriptParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.NODE_TYPE, SanyaScriptParser.ARC_TYPE, SanyaScriptParser.GRAPH_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.defvar()
                self.state = 32
                self.match(SanyaScriptParser.EQUALS)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SanyaScriptParser.T__0:
                    self.state = 33
                    self.cast()


                self.state = 36
                self.value()
                pass
            elif token in [SanyaScriptParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(SanyaScriptParser.ID)
                self.state = 39
                self.match(SanyaScriptParser.EQUALS)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SanyaScriptParser.T__0:
                    self.state = 40
                    self.cast()


                self.state = 43
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CastContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(SanyaScriptParser.TypeContext,0)


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_cast

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast" ):
                return visitor.visitCast(self)
            else:
                return visitor.visitChildren(self)




    def cast(self):

        localctx = SanyaScriptParser.CastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(SanyaScriptParser.T__0)
            self.state = 47
            self.type()
            self.state = 48
            self.match(SanyaScriptParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_defvar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefgraphContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GRAPH_TYPE(self):
            return self.getToken(SanyaScriptParser.GRAPH_TYPE, 0)
        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefgraph" ):
                return visitor.visitDefgraph(self)
            else:
                return visitor.visitChildren(self)


    class DefnodeContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NODE_TYPE(self):
            return self.getToken(SanyaScriptParser.NODE_TYPE, 0)
        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefnode" ):
                return visitor.visitDefnode(self)
            else:
                return visitor.visitChildren(self)


    class DefarcContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ARC_TYPE(self):
            return self.getToken(SanyaScriptParser.ARC_TYPE, 0)
        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefarc" ):
                return visitor.visitDefarc(self)
            else:
                return visitor.visitChildren(self)



    def defvar(self):

        localctx = SanyaScriptParser.DefvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defvar)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.NODE_TYPE]:
                localctx = SanyaScriptParser.DefnodeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(SanyaScriptParser.NODE_TYPE)
                self.state = 51
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.ARC_TYPE]:
                localctx = SanyaScriptParser.DefarcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(SanyaScriptParser.ARC_TYPE)
                self.state = 53
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.GRAPH_TYPE]:
                localctx = SanyaScriptParser.DefgraphContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(SanyaScriptParser.GRAPH_TYPE)
                self.state = 55
                self.match(SanyaScriptParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_arc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleArc" ):
                return visitor.visitSimpleArc(self)
            else:
                return visitor.visitChildren(self)


    class WeightedArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WEIGHTED_ARC_START(self):
            return self.getToken(SanyaScriptParser.WEIGHTED_ARC_START, 0)
        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)
        def WEIGHTED_ARC_END(self):
            return self.getToken(SanyaScriptParser.WEIGHTED_ARC_END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeightedArc" ):
                return visitor.visitWeightedArc(self)
            else:
                return visitor.visitChildren(self)


    class WeightedUndirectedArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WEIGHTED_UNDIRECTED_ARC_START(self):
            return self.getToken(SanyaScriptParser.WEIGHTED_UNDIRECTED_ARC_START, 0)
        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)
        def WEIGHTED_ARC_END(self):
            return self.getToken(SanyaScriptParser.WEIGHTED_ARC_END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeightedUndirectedArc" ):
                return visitor.visitWeightedUndirectedArc(self)
            else:
                return visitor.visitChildren(self)


    class SimpleUndirectedArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleUndirectedArc" ):
                return visitor.visitSimpleUndirectedArc(self)
            else:
                return visitor.visitChildren(self)



    def arc(self):

        localctx = SanyaScriptParser.ArcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arc)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.T__2]:
                localctx = SanyaScriptParser.SimpleArcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SanyaScriptParser.T__2)
                pass
            elif token in [SanyaScriptParser.T__3]:
                localctx = SanyaScriptParser.SimpleUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(SanyaScriptParser.T__3)
                pass
            elif token in [SanyaScriptParser.WEIGHTED_ARC_START]:
                localctx = SanyaScriptParser.WeightedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(SanyaScriptParser.WEIGHTED_ARC_START)
                self.state = 61
                self.match(SanyaScriptParser.INT)
                self.state = 62
                self.match(SanyaScriptParser.WEIGHTED_ARC_END)
                pass
            elif token in [SanyaScriptParser.WEIGHTED_UNDIRECTED_ARC_START]:
                localctx = SanyaScriptParser.WeightedUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(SanyaScriptParser.WEIGHTED_UNDIRECTED_ARC_START)
                self.state = 64
                self.match(SanyaScriptParser.INT)
                self.state = 65
                self.match(SanyaScriptParser.WEIGHTED_ARC_END)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GraphValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SanyaScriptParser.ValueContext)
            else:
                return self.getTypedRuleContext(SanyaScriptParser.ValueContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphValue" ):
                return visitor.visitGraphValue(self)
            else:
                return visitor.visitChildren(self)


    class NodeValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeValue" ):
                return visitor.visitNodeValue(self)
            else:
                return visitor.visitChildren(self)


    class IdValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdValue" ):
                return visitor.visitIdValue(self)
            else:
                return visitor.visitChildren(self)


    class ArcValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arc(self):
            return self.getTypedRuleContext(SanyaScriptParser.ArcContext,0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SanyaScriptParser.INT)
            else:
                return self.getToken(SanyaScriptParser.INT, i)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SanyaScriptParser.ID)
            else:
                return self.getToken(SanyaScriptParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArcValue" ):
                return visitor.visitArcValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = SanyaScriptParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = SanyaScriptParser.NodeValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(SanyaScriptParser.INT)
                pass

            elif la_ == 2:
                localctx = SanyaScriptParser.ArcValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==SanyaScriptParser.INT or _la==SanyaScriptParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.arc()
                self.state = 71
                _la = self._input.LA(1)
                if not(_la==SanyaScriptParser.INT or _la==SanyaScriptParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = SanyaScriptParser.GraphValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(SanyaScriptParser.T__4)
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 74
                        self.value()
                        self.state = 75
                        self.match(SanyaScriptParser.T__5) 
                    self.state = 81
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 82
                self.value()
                self.state = 83
                self.match(SanyaScriptParser.T__6)
                pass

            elif la_ == 4:
                localctx = SanyaScriptParser.IdValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.match(SanyaScriptParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE_TYPE(self):
            return self.getToken(SanyaScriptParser.NODE_TYPE, 0)

        def ARC_TYPE(self):
            return self.getToken(SanyaScriptParser.ARC_TYPE, 0)

        def GRAPH_TYPE(self):
            return self.getToken(SanyaScriptParser.GRAPH_TYPE, 0)

        def getRuleIndex(self):
            return SanyaScriptParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type(self):

        localctx = SanyaScriptParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SanyaScriptParser.NODE_TYPE) | (1 << SanyaScriptParser.ARC_TYPE) | (1 << SanyaScriptParser.GRAPH_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(SanyaScriptParser.PRINT, 0)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def getRuleIndex(self):
            return SanyaScriptParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print(self):

        localctx = SanyaScriptParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SanyaScriptParser.PRINT)
            self.state = 91
            self.match(SanyaScriptParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





