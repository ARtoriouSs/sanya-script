from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.AST.block import Block
from parse.AST.statements.defvar import Defvar
from parse.AST.statements.assignment import Assignment
from parse.AST.statements.print import Print
from parse.var import Var
import parse.errors as errors
import copy
from src.parse.AST.id import Id
from src.parse.AST.namespace import Namespace
from src.parse.value_visitor import ValueVisitor


class Visitor(SanyaScriptVisitor):
    def __init__(self, namespace = None):
        self.namespace = copy.copy(namespace) or Namespace()
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
        target = self.visit(ctx.defvar())
        value = self._value_visitor().visit(ctx.value())
        cast = self.visitCast(ctx.cast())
        return Assignment(target, value, cast)

    def visitReassign(self, ctx):
        name = ctx.ID().getText()
        target = Id(name) if self.namespace.has_var(name) else errors.undef(name)
        value = self._value_visitor().visit(ctx.value())
        cast = self.visitCast(ctx.cast())
        return Assignment(target, value, cast)

    def visitCast(self, ctx):
        return ctx.type().getText() if ctx else None

    def visitPrint(self, ctx):
        name = ctx.ID().getText()
        return Print(name) if self.namespace.has_var(name) else errors.undef(name)

    def _add_var(self, type, name):
        self.namespace.add_var(Var(type, name))
        return Defvar(type, name)

    def _value_visitor(self):
        return ValueVisitor(self.block, self.namespace)
