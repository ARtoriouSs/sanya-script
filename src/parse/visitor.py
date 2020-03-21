from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.grammar.SanyaScriptParser import SanyaScriptParser
from parse.AST.block import Block
from parse.AST.defvar import Defvar
from parse.AST.assignment import Assignment

class Visitor(SanyaScriptVisitor):
    def __init__(self):
        self.block = Block()

    def visitSanyaScript(self, ctx):
        for statement in ctx.statement():
            self.block.add_statement(self.visitStatement(statement))
        return self.block

    def visitStatement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDefnode(self, ctx):
        return Defvar("node", ctx.ID().getText())

    def visitDefarc(self, ctx):
        return Defvar("arc", ctx.ID().getText())

    def visitDefgraph(self, ctx):
        return Defvar("graph", ctx.ID().getText())

    def visitAssign(self, ctx):
        pass

    def visitReassign(self, ctx):
        pass

    def visitPrint(self, ctx):
        pass
