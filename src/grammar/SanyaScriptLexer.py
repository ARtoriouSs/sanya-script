# Generated from src/grammar/SanyaScript.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\7\25o\n\25\f\25\16\25r\13\25\3\26\3\26\7\26v\n\26\f\26")
        buf.write("\16\26y\13\26\3\27\6\27|\n\27\r\27\16\27}\3\27\3\27\3")
        buf.write("\30\3\30\6\30\u0084\n\30\r\30\16\30\u0085\3\30\3\30\2")
        buf.write("\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\3\2\b\3\2\63;\3\2\62;\3\2c|\5\2\62;C\\c|\5\2\13\f")
        buf.write("\17\17\"\"\3\2\f\f\2\u008c\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\63")
        buf.write("\3\2\2\2\7\65\3\2\2\2\t8\3\2\2\2\13<\3\2\2\2\r>\3\2\2")
        buf.write("\2\17@\3\2\2\2\21B\3\2\2\2\23G\3\2\2\2\25K\3\2\2\2\27")
        buf.write("Q\3\2\2\2\31T\3\2\2\2\33X\3\2\2\2\35\\\3\2\2\2\37b\3\2")
        buf.write("\2\2!d\3\2\2\2#f\3\2\2\2%h\3\2\2\2\'j\3\2\2\2)l\3\2\2")
        buf.write("\2+s\3\2\2\2-{\3\2\2\2/\u0081\3\2\2\2\61\62\7*\2\2\62")
        buf.write("\4\3\2\2\2\63\64\7+\2\2\64\6\3\2\2\2\65\66\7/\2\2\66\67")
        buf.write("\7@\2\2\67\b\3\2\2\289\7>\2\29:\7/\2\2:;\7@\2\2;\n\3\2")
        buf.write("\2\2<=\7]\2\2=\f\3\2\2\2>?\7.\2\2?\16\3\2\2\2@A\7_\2\2")
        buf.write("A\20\3\2\2\2BC\7p\2\2CD\7q\2\2DE\7f\2\2EF\7g\2\2F\22\3")
        buf.write("\2\2\2GH\7c\2\2HI\7t\2\2IJ\7e\2\2J\24\3\2\2\2KL\7i\2\2")
        buf.write("LM\7t\2\2MN\7c\2\2NO\7r\2\2OP\7j\2\2P\26\3\2\2\2QR\7/")
        buf.write("\2\2RS\7]\2\2S\30\3\2\2\2TU\7>\2\2UV\7/\2\2VW\7]\2\2W")
        buf.write("\32\3\2\2\2XY\7_\2\2YZ\7/\2\2Z[\7@\2\2[\34\3\2\2\2\\]")
        buf.write("\7r\2\2]^\7t\2\2^_\7k\2\2_`\7p\2\2`a\7v\2\2a\36\3\2\2")
        buf.write("\2bc\7?\2\2c \3\2\2\2de\7-\2\2e\"\3\2\2\2fg\7/\2\2g$\3")
        buf.write("\2\2\2hi\7,\2\2i&\3\2\2\2jk\7\61\2\2k(\3\2\2\2lp\t\2\2")
        buf.write("\2mo\t\3\2\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q")
        buf.write("*\3\2\2\2rp\3\2\2\2sw\t\4\2\2tv\t\5\2\2ut\3\2\2\2vy\3")
        buf.write("\2\2\2wu\3\2\2\2wx\3\2\2\2x,\3\2\2\2yw\3\2\2\2z|\t\6\2")
        buf.write("\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0080\b\27\2\2\u0080.\3\2\2\2\u0081\u0083\7%\2")
        buf.write("\2\u0082\u0084\n\7\2\2\u0083\u0082\3\2\2\2\u0084\u0085")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\b\30\2\2\u0088\60\3\2\2\2\7")
        buf.write("\2pw}\u0085\3\b\2\2")
        return buf.getvalue()


class SanyaScriptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NODE_TYPE = 8
    ARC_TYPE = 9
    GRAPH_TYPE = 10
    WEIGHTED_ARC_START = 11
    WEIGHTED_UNDIRECTED_ARC_START = 12
    WEIGHTED_ARC_END = 13
    PRINT = 14
    EQUALS = 15
    PLUS = 16
    MINUS = 17
    MULT = 18
    DIV = 19
    INT = 20
    ID = 21
    WS = 22
    COMMENT = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'->'", "'<->'", "'['", "','", "']'", "'node'", 
            "'arc'", "'graph'", "'-['", "'<-['", "']->'", "'print'", "'='", 
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "NODE_TYPE", "ARC_TYPE", "GRAPH_TYPE", "WEIGHTED_ARC_START", 
            "WEIGHTED_UNDIRECTED_ARC_START", "WEIGHTED_ARC_END", "PRINT", 
            "EQUALS", "PLUS", "MINUS", "MULT", "DIV", "INT", "ID", "WS", 
            "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NODE_TYPE", "ARC_TYPE", "GRAPH_TYPE", "WEIGHTED_ARC_START", 
                  "WEIGHTED_UNDIRECTED_ARC_START", "WEIGHTED_ARC_END", "PRINT", 
                  "EQUALS", "PLUS", "MINUS", "MULT", "DIV", "INT", "ID", 
                  "WS", "COMMENT" ]

    grammarFileName = "SanyaScript.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


