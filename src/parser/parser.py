from antlr4 import *

from parser.grammar.SanyaScriptLexer import SanyaScriptLexer
from parser.grammar.SanyaScriptParser import SanyaScriptParser
from parser.visitors.visitor import Visitor


class Parser:
    @classmethod
    def parse(self, filepath):
        input_stream = FileStream(filepath)
        lexer = SanyaScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SanyaScriptParser(stream)
        tree = parser.sanyaScript()

        visitor = Visitor()
        return visitor.visitSanyaScript(tree)
