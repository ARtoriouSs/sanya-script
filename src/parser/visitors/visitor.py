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
from parser.AST.statements.println import Println
from parser.AST.statements.return_stat import ReturnStat
from parser.AST.statements.if_stat import IfStat
from parser.AST.statements.push_to_array import PushToArray
from parser.AST.statements.while_cycle import WhileCycle
from parser.AST.id import Id


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

    def visitDefvar(self, ctx):
        return self._add_var(ctx.type_().getText(), ctx.ID().getText())

    def visitAssign(self, ctx):
        target = self.visit(ctx.defvar())
        value = self._value_visitor().visit(ctx.value())
        if target.type != value.return_type() and value.return_type() != "nope":
            ParseError.type_error(target.name, value.return_type(), target.type)
        return Assignment(target, value)

    def visitReassign(self, ctx):
        name = ctx.ID().getText()
        target = Id(name)
        value = self._value_visitor().visit(ctx.value())

        var = self.namespace.find_var(name)
        if var is None: ParseError.undef(name)
        if var.type != value.return_type() and value.return_type() != "nope":
            ParseError.type_error(name, value.return_type(), var.type)

        return Assignment(target, value)

    def visitPrintStat(self, ctx):
        return PrintStat(self._value_visitor().visit(ctx.value()))

    def visitPrintln(self, ctx):
        return Println(self._value_visitor().visit(ctx.value()))

    def visitPushToArray(self, ctx):
        value = self._value_visitor().visit(ctx.value())
        name = ctx.ID().getText()

        var = self.namespace.find_var(name)
        if var is None: ParseError.undef(name)
        if var.type != value.return_type() + "{}" and value.return_type() != "nope":
            ParseError.array_value_error(name, value.return_type(), var.type)

        return PushToArray(name, value)

    def visitReturnStat(self, ctx):
        return ReturnStat(self._value_visitor().visit(ctx.value()))

    def visitDeffun(self, ctx):
        return self._funciton_visitor().visit(ctx)

    def visitFunCall(self, ctx):
        return self._funciton_visitor().visit(ctx)

    def visitIfStat(self, ctx):
        condition = self._value_visitor().visit(ctx.value())
        then, else_ = self.visit(ctx.ifBlock())
        return IfStat(condition, then, else_)

    def visitIfThenBlock(self, ctx):
        then = self._visitor().visitSanyaScript(ctx.then)
        return [then, None]

    def visitIfThenElseBlock(self, ctx):
        then = self._visitor().visitSanyaScript(ctx.then)
        else_ = self._visitor().visitSanyaScript(ctx.else_)
        return [then, else_]

    def visitWhileCycle(self, ctx):
        condition = self._value_visitor().visit(ctx.value())
        block = self._funciton_visitor().visit(ctx.block())
        return WhileCycle(condition, block)

    def _add_var(self, type_, name):
        self.namespace.add_var(name, type_)
        return Defvar(type_, name)

    def _value_visitor(self):
        return ValueVisitor(self.block, self.namespace)

    def _funciton_visitor(self):
        return FunctionVisitior(self.block, self.namespace)

    def _visitor(self):
        return self.__class__(self.namespace)
