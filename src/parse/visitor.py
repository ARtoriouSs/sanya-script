from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.grammar.SanyaScriptParser import SanyaScriptParser
from parse.AST.block import Block
from parse.AST.statements.defvar import Defvar
from parse.AST.statements.assignment import Assignment
from parse.AST.statements.print import Print
from parse.var import Var
import parse.errors as errors


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
        return self._add_var("node", ctx.ID().getText())

    def visitDefarc(self, ctx):
        return self._add_var("arc", ctx.ID().getText())

    def visitDefgraph(self, ctx):
        return self._add_var("graph", ctx.ID().getText())

    def visitAssign(self, ctx):
        pass

    def visitReassign(self, ctx):
        pass

    def visitPrint(self, ctx):
        name = ctx.ID().getText()
        if self.block.namespace.has(name):
            return Print(name)
        else:
            errors.undef(name)

    def _add_var(self, type, name):
        self.block.namespace.add_var(Var(type, name))
        return Defvar(type, name)
