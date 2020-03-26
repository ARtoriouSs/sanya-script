from antlr4 import *
from parse.grammar.SanyaScriptLexer import SanyaScriptLexer
from parse.grammar.SanyaScriptParser import SanyaScriptParser
from parse.visitors.visitor import Visitor


class Parser:
    @classmethod
    def parse(self, filepath=None, code=None):
        input_stream = FileStream(filepath) if filepath else InputStream(code)
        lexer = SanyaScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SanyaScriptParser(stream)
        tree = parser.sanyaScript()

        visitor = Visitor()
        return visitor.visitSanyaScript(tree)
