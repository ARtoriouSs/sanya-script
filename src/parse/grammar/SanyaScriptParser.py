# Generated from src/parse/grammar/SanyaScript.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\5\4")
        buf.write("\'\n\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\4\5\4\61\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b[\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\2\2\f")
        buf.write("\2\4\6\b\n\f\16\20\22\24\2\4\3\2\26\27\3\2\r\17\2h\2\31")
        buf.write("\3\2\2\2\4!\3\2\2\2\6\60\3\2\2\2\b\62\3\2\2\2\n<\3\2\2")
        buf.write("\2\fF\3\2\2\2\16Z\3\2\2\2\20\\\3\2\2\2\22^\3\2\2\2\24")
        buf.write("`\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\33\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2")
        buf.write("\34\35\7\2\2\3\35\3\3\2\2\2\36\"\5\n\6\2\37\"\5\6\4\2")
        buf.write(" \"\5\24\13\2!\36\3\2\2\2!\37\3\2\2\2! \3\2\2\2\"\5\3")
        buf.write("\2\2\2#$\5\n\6\2$&\7\21\2\2%\'\5\b\5\2&%\3\2\2\2&\'\3")
        buf.write("\2\2\2\'(\3\2\2\2()\5\16\b\2)\61\3\2\2\2*+\7\27\2\2+-")
        buf.write("\7\21\2\2,.\5\b\5\2-,\3\2\2\2-.\3\2\2\2./\3\2\2\2/\61")
        buf.write("\5\16\b\2\60#\3\2\2\2\60*\3\2\2\2\61\7\3\2\2\2\62\63\7")
        buf.write("\3\2\2\63\64\5\22\n\2\64\65\7\4\2\2\65\t\3\2\2\2\66\67")
        buf.write("\7\r\2\2\67=\7\27\2\289\7\16\2\29=\7\27\2\2:;\7\17\2\2")
        buf.write(";=\7\27\2\2<\66\3\2\2\2<8\3\2\2\2<:\3\2\2\2=\13\3\2\2")
        buf.write("\2>G\7\5\2\2?G\7\6\2\2@A\7\7\2\2AB\7\26\2\2BG\7\b\2\2")
        buf.write("CD\7\t\2\2DE\7\26\2\2EG\7\b\2\2F>\3\2\2\2F?\3\2\2\2F@")
        buf.write("\3\2\2\2FC\3\2\2\2G\r\3\2\2\2H[\7\26\2\2IJ\5\20\t\2JK")
        buf.write("\5\f\7\2KL\5\20\t\2L[\3\2\2\2MS\7\n\2\2NO\5\16\b\2OP\7")
        buf.write("\13\2\2PR\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2")
        buf.write("\2\2TV\3\2\2\2US\3\2\2\2VW\5\16\b\2WX\7\f\2\2X[\3\2\2")
        buf.write("\2Y[\7\27\2\2ZH\3\2\2\2ZI\3\2\2\2ZM\3\2\2\2ZY\3\2\2\2")
        buf.write("[\17\3\2\2\2\\]\t\2\2\2]\21\3\2\2\2^_\t\3\2\2_\23\3\2")
        buf.write("\2\2`a\7\20\2\2ab\7\27\2\2b\25\3\2\2\2\13\31!&-\60<FS")
        buf.write("Z")
        return buf.getvalue()


class SanyaScriptParser ( Parser ):

    grammarFileName = "SanyaScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'->'", "'<->'", "'-['", 
                     "']->'", "'<-['", "'['", "','", "']'", "'node'", "'arc'", 
                     "'graph'", "'print'", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NODE_TYPE", 
                      "ARC_TYPE", "GRAPH_TYPE", "PRINT", "EQUALS", "PLUS", 
                      "MINUS", "MULT", "DIV", "INT", "ID", "WS", "COMMENT" ]

    RULE_sanyaScript = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_cast = 3
    RULE_defvar = 4
    RULE_arc = 5
    RULE_value = 6
    RULE_arcPart = 7
    RULE_type = 8
    RULE_print = 9

    ruleNames =  [ "sanyaScript", "statement", "assignment", "cast", "defvar", 
                   "arc", "value", "arcPart", "type", "print" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    NODE_TYPE=11
    ARC_TYPE=12
    GRAPH_TYPE=13
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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SanyaScriptParser.NODE_TYPE) | (1 << SanyaScriptParser.ARC_TYPE) | (1 << SanyaScriptParser.GRAPH_TYPE) | (1 << SanyaScriptParser.PRINT) | (1 << SanyaScriptParser.ID))) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.defvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
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


        def getRuleIndex(self):
            return SanyaScriptParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReassignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)
        def EQUALS(self):
            return self.getToken(SanyaScriptParser.EQUALS, 0)
        def value(self):
            return self.getTypedRuleContext(SanyaScriptParser.ValueContext,0)

        def cast(self):
            return self.getTypedRuleContext(SanyaScriptParser.CastContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReassign" ):
                return visitor.visitReassign(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def defvar(self):
            return self.getTypedRuleContext(SanyaScriptParser.DefvarContext,0)

        def EQUALS(self):
            return self.getToken(SanyaScriptParser.EQUALS, 0)
        def value(self):
            return self.getTypedRuleContext(SanyaScriptParser.ValueContext,0)

        def cast(self):
            return self.getTypedRuleContext(SanyaScriptParser.CastContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = SanyaScriptParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.NODE_TYPE, SanyaScriptParser.ARC_TYPE, SanyaScriptParser.GRAPH_TYPE]:
                localctx = SanyaScriptParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.defvar()
                self.state = 34
                self.match(SanyaScriptParser.EQUALS)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SanyaScriptParser.T__0:
                    self.state = 35
                    self.cast()


                self.state = 38
                self.value()
                pass
            elif token in [SanyaScriptParser.ID]:
                localctx = SanyaScriptParser.ReassignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(SanyaScriptParser.ID)
                self.state = 41
                self.match(SanyaScriptParser.EQUALS)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SanyaScriptParser.T__0:
                    self.state = 42
                    self.cast()


                self.state = 45
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
            self.state = 48
            self.match(SanyaScriptParser.T__0)
            self.state = 49
            self.type()
            self.state = 50
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.NODE_TYPE]:
                localctx = SanyaScriptParser.DefnodeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(SanyaScriptParser.NODE_TYPE)
                self.state = 53
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.ARC_TYPE]:
                localctx = SanyaScriptParser.DefarcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(SanyaScriptParser.ARC_TYPE)
                self.state = 55
                self.match(SanyaScriptParser.ID)
                pass
            elif token in [SanyaScriptParser.GRAPH_TYPE]:
                localctx = SanyaScriptParser.DefgraphContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(SanyaScriptParser.GRAPH_TYPE)
                self.state = 57
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

        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeightedArc" ):
                return visitor.visitWeightedArc(self)
            else:
                return visitor.visitChildren(self)


    class WeightedUndirectedArcContext(ArcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SanyaScriptParser.ArcContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)

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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SanyaScriptParser.T__2]:
                localctx = SanyaScriptParser.SimpleArcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(SanyaScriptParser.T__2)
                pass
            elif token in [SanyaScriptParser.T__3]:
                localctx = SanyaScriptParser.SimpleUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(SanyaScriptParser.T__3)
                pass
            elif token in [SanyaScriptParser.T__4]:
                localctx = SanyaScriptParser.WeightedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(SanyaScriptParser.T__4)
                self.state = 63
                self.match(SanyaScriptParser.INT)
                self.state = 64
                self.match(SanyaScriptParser.T__5)
                pass
            elif token in [SanyaScriptParser.T__6]:
                localctx = SanyaScriptParser.WeightedUndirectedArcContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(SanyaScriptParser.T__6)
                self.state = 66
                self.match(SanyaScriptParser.INT)
                self.state = 67
                self.match(SanyaScriptParser.T__5)
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

        def arcPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SanyaScriptParser.ArcPartContext)
            else:
                return self.getTypedRuleContext(SanyaScriptParser.ArcPartContext,i)

        def arc(self):
            return self.getTypedRuleContext(SanyaScriptParser.ArcContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArcValue" ):
                return visitor.visitArcValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = SanyaScriptParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = SanyaScriptParser.NodeValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(SanyaScriptParser.INT)
                pass

            elif la_ == 2:
                localctx = SanyaScriptParser.ArcValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.arcPart()
                self.state = 72
                self.arc()
                self.state = 73
                self.arcPart()
                pass

            elif la_ == 3:
                localctx = SanyaScriptParser.GraphValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(SanyaScriptParser.T__7)
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 76
                        self.value()
                        self.state = 77
                        self.match(SanyaScriptParser.T__8) 
                    self.state = 83
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 84
                self.value()
                self.state = 85
                self.match(SanyaScriptParser.T__9)
                pass

            elif la_ == 4:
                localctx = SanyaScriptParser.IdValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(SanyaScriptParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArcPartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SanyaScriptParser.INT, 0)

        def ID(self):
            return self.getToken(SanyaScriptParser.ID, 0)

        def getRuleIndex(self):
            return SanyaScriptParser.RULE_arcPart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArcPart" ):
                return visitor.visitArcPart(self)
            else:
                return visitor.visitChildren(self)




    def arcPart(self):

        localctx = SanyaScriptParser.ArcPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arcPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(_la==SanyaScriptParser.INT or _la==SanyaScriptParser.ID):
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
        self.enterRule(localctx, 16, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
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
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SanyaScriptParser.PRINT)
            self.state = 95
            self.match(SanyaScriptParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





