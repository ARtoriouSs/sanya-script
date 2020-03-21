from grammar.SanyaScriptVisitor import SanyaScriptVisitor
from grammar.SanyaScriptParser import SanyaScriptParser
from domain.ast import AST
from domain.defvar import Defvar
from domain.assignment import Assignment

class Visitor(SanyaScriptVisitor):
    def __init__(self):
        self.ast = AST()

    def visitSanyaScript(self, ctx):
        for statement in ctx.statement():
            self.ast.add_statement(self.visitStatement(statement))
        return self.ast

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
