import re

from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.visitors.function_visitor import FunctionVisitior
from parser.AST.values.graph import Graph
from parser.AST.values.node import Node
from parser.AST.values.arc import Arc
from parser.AST.values.num import Num
from parser.AST.values.id import Id
from parser.AST.values.fun_call import FunCall
from parser.AST.values.logic import Logic
from parser.AST.values.nope import Nope
from parser.AST.values.operations.summation import Summation
from parser.AST.values.operations.subtraction import Subtraction
from parser.AST.values.operations.multiplication import Multiplication
from parser.AST.values.operations.division import Division
from parser.AST.values.operations.not_ import Not
from parser.AST.values.operations.or_ import Or
from parser.AST.values.operations.and_ import And
from parser.AST.values.operations.equal import Equal
from parser.AST.values.operations.not_equal import NotEqual
from parser.AST.values.operations.greater_or_equal import GreaterOrEqual
from parser.AST.values.operations.less_or_equal import LessOrEqual
from parser.AST.values.operations.greater import Greater
from parser.AST.values.operations.less import Less


class ValueVisitor(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitCastValue(self, ctx):
        return self.visit(ctx.value()).cast(self.visitCast(ctx.cast()))

    def visitParenthesizedValue(self, ctx):
        return self.visit(ctx.value())

    def visitIndexValue(self, ctx):
        value = self.visit(ctx.target)
        index = self.visit(ctx.index)
        return value.set_index(index)

    def visitDivMultValue(self, ctx):
        return self._visit_binary_operation(ctx)

    def visitSumSubtrValue(self, ctx):
        return self._visit_binary_operation(ctx)

    def visitAndValue(self, ctx):
        return self._visit_binary_operation(ctx)

    def visitOrValue(self, ctx):
        return self._visit_binary_operation(ctx)

    def visitNotValue(self, ctx):
        target = self.visit(ctx.value())
        return Not(target)

    def visitComparisonValue(self, ctx):
        return self._visit_binary_operation(ctx)

    def visitNodeValue(self, ctx):
        return Node(self.visit(ctx.value()))

    def visitArcValue(self, ctx):
        source = self.visit(ctx.source)
        target = self.visit(ctx.target)
        type_, weight = self.visit(ctx.arc())
        return Arc(source, target, weight, type_)

    def visitGraphValue(self, ctx):
        elements = self.visit(ctx.graphPart()) if ctx.graphPart() is not None else []
        return Graph(elements)

    def visitGraphPart(self, ctx):
        value = self.visit(ctx.value())
        rest = self.visit(ctx.graphPart()) if ctx.graphPart() is not None else []
        return [value] + rest

    def visitNumValue(self, ctx):
        return Num(float(ctx.NUM().getText()))

    def visitIdValue(self, ctx):
        var = self.namespace.find_var(ctx.ID().getText())
        return Id(var)

    def visitFunCallValue(self, ctx):
        fun_call = self._function_visitor().visit(ctx.funCall())
        return FunCall(fun_call)

    def visitLogicValue(self, ctx):
        value = True if ctx.yes else False
        return Logic(value)

    def visitNopeValue(self, ctx):
        return Nope()

    def visitArrayPart(self, ctx):
        value = self.visit(ctx.value())
        rest = self.visit(ctx.arrayPart()) if ctx.paramValue() else []
        return [value] + rest

    def visitSimpleArc(self, ctx):
        return ["directed", 0]

    def visitSimpleUndirectedArc(self, ctx):
        return ["undirected", 0]

    def visitWeightedArc(self, ctx):
        return ["directed", float(ctx.NUM().getText())]

    def visitWeightedUndirectedArc(self, ctx):
        return ["undirected", float(ctx.NUM().getText())]

    def visitCast(self, ctx):
        return ctx.type_().getText() if ctx else None

    def _visit_binary_operation(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = ctx.operation.text
        if operation == "*":
            return Multiplication(left, right)
        elif operation == "/":
            return Division(left, right)
        elif operation == "+":
            return Summation(left, right)
        elif operation == "-":
            return Subtraction(left, right)
        elif operation == "==":
            return Equal(left, right)
        elif operation == "!=":
            return NotEqual(left, right)
        elif operation == ">=":
            return GreaterOrEqual(left, right)
        elif operation == "<=":
            return LessOrEqual(left, right)
        elif operation == ">":
            return Greater(left, right)
        elif operation == "<":
            return Less(left, right)
        elif operation == "and":
            return And(left, right)
        elif operation == "or":
            return Or(left, right)

    def _function_visitor(self):
        return FunctionVisitior(self.block, self.namespace)
