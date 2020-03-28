from parse.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parse.AST.block import Block
from parse.AST.statements.defvar import Defvar
from parse.AST.statements.assignment import Assignment
from parse.AST.statements.print import Print
from parse.AST.statements.return_stat import ReturnStat
from parse.parse_error import ParseError
import copy
from parse.AST.statements.id import Id
from parse.namespace import Namespace
from parse.visitors.value_visitor import ValueVisitor
from parse.visitors.function_visitor import FunctionVisitior


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
        return Assignment(target, value)

    def visitReassign(self, ctx):
        name = ctx.ID().getText()
        target = Id(name) if self.namespace.has_var(name) else ParseError.undef(name)
        value = self._value_visitor().visit(ctx.value())
        return Assignment(target, value)

    def visitPrint(self, ctx):
        return Print(self._value_visitor().visit(ctx.value()))

    def visitReturnStat(self, ctx):
        return ReturnStat(self._value_visitor().visit(ctx.value()))

    def visitDeffun(self, ctx):
        return self._funciton_visitor().visit(ctx)

    def visitFunCall(self, ctx):
        return self._funciton_visitor().visit(ctx)

    def _add_var(self, type_, name):
        self.namespace.add_var(name, type_)
        return Defvar(type_, name)

    def _value_visitor(self):
        return ValueVisitor(self.block, self.namespace)

    def _funciton_visitor(self):
        return FunctionVisitior(self.block, self.namespace)
