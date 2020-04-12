from antlr4 import *

from parser.grammar.SanyaScriptLexer import SanyaScriptLexer
from parser.grammar.SanyaScriptParser import SanyaScriptParser
from parser.visitors.visitor import Visitor
from parser.namespace import Namespace


class Parser:
    def __init__(self, filepath, namespace_files=()):
        self.filepath = filepath
        self.namespace_files = list(namespace_files)

    def parse(self):
        visitor = Visitor(self.initial_namespace())
        return visitor.visitSanyaScript(self._parse_tree(self.filepath))

    def initial_namespace(self):
        namespace = Namespace()
        for namespace_file in self.namespace_files:
            tree = self._parse_tree(namespace_file)
            visitor = Visitor()
            visitor.visitSanyaScript(tree)
            namespace.merge(visitor.namespace)
        return namespace

    def _parse_tree(self, filepath):
        input_stream = FileStream(filepath)
        lexer = SanyaScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SanyaScriptParser(stream)
        return parser.sanyaScript()
