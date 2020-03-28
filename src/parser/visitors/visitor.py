import copy

from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.visitors.value_visitor import ValueVisitor
from parser.visitors.function_visitor import FunctionVisitior
from parser.parse_error import ParseError
from parser.namespace import Namespace
from parser.AST.block import Block
from parser.AST.statements.defvar import Defvar
from parser.AST.statements.assignment import Assignment
from parser.AST.statements.print_stat import PrintStat
from parser.AST.statements.return_stat import ReturnStat
from parser.AST.statements.id import Id


class Visitor(SanyaScriptVisitor):
    def __init__(self, namespace=None):
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
        if target.type != value.return_type():
            ParseError.type_error(target.name, value.return_type(), target.type)
        return Assignment(target, value)

    def visitReassign(self, ctx):
        name = ctx.ID().getText()
        target = Id(name)
        value = self._value_visitor().visit(ctx.value())

        var = self.namespace.find_var(name)
        if var is None: ParseError.undef(name)
        if var.type != value.return_type(): ParseError.type_error(name, value.return_type(), var.type)

        return Assignment(target, value)

    def visitPrintStat(self, ctx):
        return PrintStat(self._value_visitor().visit(ctx.value()))

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