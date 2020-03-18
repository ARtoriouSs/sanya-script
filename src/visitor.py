from grammar.SanyaScriptVisitor import SanyaScriptVisitor
from grammar.SanyaScriptParser import SanyaScriptParser

class Visitor(SanyaScriptVisitor):
    def __init__(self):
        self.ast = {}
