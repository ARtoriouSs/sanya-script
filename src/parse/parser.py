from antlr4 import *
from parse.grammar.SanyaScriptLexer import SanyaScriptLexer
from parse.grammar.SanyaScriptParser import SanyaScriptParser
from parse.visitor import Visitor


class Parser:
    def parse(self, filename):
        input_stream = FileStream(filename)
        lexer = SanyaScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SanyaScriptParser(stream)
        tree = parser.sanyaScript()

        visitor = Visitor()
        return visitor.visitSanyaScript(tree)
