# Generated from src/grammar/SanyaScript.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\5\4%\n\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\64")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7>\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bI\n\b\f\b\16\bL\13\b\3")
        buf.write("\b\3\b\3\b\3\b\5\bR\n\b\3\t\3\t\3\n\3\n\3\n\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\4\3\2\26\27\3\2\n\f\2]\2\27\3")
        buf.write("\2\2\2\4\37\3\2\2\2\6!\3\2\2\2\b(\3\2\2\2\n\63\3\2\2\2")
        buf.write("\f=\3\2\2\2\16Q\3\2\2\2\20S\3\2\2\2\22U\3\2\2\2\24\26")
        buf.write("\5\4\3\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27")
        buf.write("\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\2\2\3")
        buf.write("\33\3\3\2\2\2\34 \5\n\6\2\35 \5\6\4\2\36 \5\22\n\2\37")
        buf.write("\34\3\2\2\2\37\35\3\2\2\2\37\36\3\2\2\2 \5\3\2\2\2!\"")
        buf.write("\5\n\6\2\"$\7\21\2\2#%\5\b\5\2$#\3\2\2\2$%\3\2\2\2%&\3")
        buf.write("\2\2\2&\'\5\16\b\2\'\7\3\2\2\2()\7\3\2\2)*\5\20\t\2*+")
        buf.write("\7\4\2\2+\t\3\2\2\2,-\7\n\2\2-\64\7\27\2\2./\7\13\2\2")
        buf.write("/\64\7\27\2\2\60\61\7\f\2\2\61\64\7\27\2\2\62\64\7\27")
        buf.write("\2\2\63,\3\2\2\2\63.\3\2\2\2\63\60\3\2\2\2\63\62\3\2\2")
        buf.write("\2\64\13\3\2\2\2\65>\7\5\2\2\66>\7\6\2\2\678\7\r\2\28")
        buf.write("9\7\26\2\29>\7\17\2\2:;\7\16\2\2;<\7\26\2\2<>\7\17\2\2")
        buf.write("=\65\3\2\2\2=\66\3\2\2\2=\67\3\2\2\2=:\3\2\2\2>\r\3\2")
        buf.write("\2\2?R\7\26\2\2@A\t\2\2\2AB\5\f\7\2BC\t\2\2\2CR\3\2\2")
        buf.write("\2DJ\7\7\2\2EF\5\16\b\2FG\7\b\2\2GI\3\2\2\2HE\3\2\2\2")
        buf.write("IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\5")
        buf.write("\16\b\2NO\7\t\2\2OR\3\2\2\2PR\7\27\2\2Q?\3\2\2\2Q@\3\2")
        buf.write("\2\2QD\3\2\2\2QP\3\2\2\2R\17\3\2\2\2ST\t\3\2\2T\21\3\2")
        buf.write("\2\2UV\7\20\2\2VW\7\27\2\2W\23\3\2\2\2\t\27\37$\63=JQ")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSanyaScript" ):
                listener.enterSanyaScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSanyaScript" ):
                listener.exitSanyaScript(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




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


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SanyaScriptParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast" ):
                listener.enterCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast" ):
                listener.exitCast(self)




    def cast(self):

        localctx = SanyaScriptParser.CastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cast)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SanyaScriptParser.T__0)
            self.state = 39
            self.type()
            self.state = 40
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefgraph" ):
                listener.enterDefgraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefgraph" ):
                listener.exitDefgraph(self)


    class RedefContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedef" ):
                listener.enterRedef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedef" ):
                listener.exitRedef(self)


    class DefnodeContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NODE_TYPE(self):
            return self.getToken(SanyaScriptParser.NODE_TYPE, 0)
        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefnode" ):
                listener.enterDefnode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefnode" ):
                listener.exitDefnode(self)


    class DefarcContext(DefvarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.DefvarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ARC_TYPE(self):
            return self.getToken(SanyaScriptParser.ARC_TYPE, 0)
        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefarc" ):
                listener.enterDefarc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefarc" ):
                listener.exitDefarc(self)



    def defvar(self):

        localctx = SanyaScriptParser.DefvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defvar)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.NODE_TYPE]:
                localctx = SanyaScriptParser.DefnodeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(SanyaScriptParser.NODE_TYPE)
                self.state = 43
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.ARC_TYPE]:
                localctx = SanyaScriptParser.DefarcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(SanyaScriptParser.ARC_TYPE)
                self.state = 45
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.GRAPH_TYPE]:
                localctx = SanyaScriptParser.DefgraphContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(SanyaScriptParser.GRAPH_TYPE)
                self.state = 47
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.ID]:
                localctx = SanyaScriptParser.RedefContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleArc" ):
                listener.enterSimpleArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleArc" ):
                listener.exitSimpleArc(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeightedArc" ):
                listener.enterWeightedArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeightedArc" ):
                listener.exitWeightedArc(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeightedUndirectedArc" ):
                listener.enterWeightedUndirectedArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeightedUndirectedArc" ):
                listener.exitWeightedUndirectedArc(self)


    class SimpleUndirectedArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleUndirectedArc" ):
                listener.enterSimpleUndirectedArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleUndirectedArc" ):
                listener.exitSimpleUndirectedArc(self)



    def arc(self):

        localctx = SanyaScriptParser.ArcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arc)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.T__2]:
                localctx = SanyaScriptParser.SimpleArcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(SanyaScriptParser.T__2)
                pass
            elif token in [SanyaScriptParser.T__3]:
                localctx = SanyaScriptParser.SimpleUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(SanyaScriptParser.T__3)
                pass
            elif token in [SanyaScriptParser.WEIGHTED_ARC_START]:
                localctx = SanyaScriptParser.WeightedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(SanyaScriptParser.WEIGHTED_ARC_START)
                self.state = 54
                self.match(SanyaScriptParser.INT)
                self.state = 55
                self.match(SanyaScriptParser.WEIGHTED_ARC_END)
                pass
            elif token in [SanyaScriptParser.WEIGHTED_UNDIRECTED_ARC_START]:
                localctx = SanyaScriptParser.WeightedUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(SanyaScriptParser.WEIGHTED_UNDIRECTED_ARC_START)
                self.state = 57
                self.match(SanyaScriptParser.INT)
                self.state = 58
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphValue" ):
                listener.enterGraphValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphValue" ):
                listener.exitGraphValue(self)


    class NodeValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeValue" ):
                listener.enterNodeValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeValue" ):
                listener.exitNodeValue(self)


    class IdValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdValue" ):
                listener.enterIdValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdValue" ):
                listener.exitIdValue(self)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArcValue" ):
                listener.enterArcValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArcValue" ):
                listener.exitArcValue(self)



    def value(self):

        localctx = SanyaScriptParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = SanyaScriptParser.NodeValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(SanyaScriptParser.INT)
                pass

            elif la_ == 2:
                localctx = SanyaScriptParser.ArcValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                _la = self._input.LA(1)
                if not(_la==SanyaScriptParser.INT or _la==SanyaScriptParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.arc()
                self.state = 64
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
                self.state = 66
                self.match(SanyaScriptParser.T__4)
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 67
                        self.value()
                        self.state = 68
                        self.match(SanyaScriptParser.T__5) 
                    self.state = 74
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 75
                self.value()
                self.state = 76
                self.match(SanyaScriptParser.T__6)
                pass

            elif la_ == 4:
                localctx = SanyaScriptParser.IdValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type(self):

        localctx = SanyaScriptParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print(self):

        localctx = SanyaScriptParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SanyaScriptParser.PRINT)
            self.state = 84
            self.match(SanyaScriptParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





