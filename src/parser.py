import sys

from antlr4 import *
from grammar.SanyaScriptLexer import SanyaScriptLexer
from grammar.SanyaScriptParser import SanyaScriptParser
from visitor import Visitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SanyaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SanyaScriptParser(stream)
    tree = parser.sanyaScript()
    visitor = Visitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
