from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.parse_error import ParseError
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
from parser.AST.values.operations.validator import Validator


class ValueVisitor(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitParenthesizedValue(self, ctx):
        return self.visit(ctx.value()).cast(self.visitCast(ctx.cast()))

    def visitDivMultValue(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = ctx.operation.text
        if not Validator(operation, left, right):
            ParseError.incompatible_operation(operation, left.return_type(), right.return_type())
        if operation == "*":
            return Multiplication(left, right)
        elif operation == "/":
            return Division(left, right)

    def visitSumSubtrValue(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = ctx.operation.text
        if not Validator(operation, left, right):
            ParseError.incompatible_operation(operation, left.return_type(), right.return_type())
        if operation == "+":
            return Summation(left, right)
        elif operation == "-":
            return Subtraction(left, right)

    def visitAndValue(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if not Validator("and", left, right):
            ParseError.incompatible_operation("not", left.return_type(), right.return_type())
        return And(left, right)

    def visitOrValue(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if not Validator("or", left, right):
            ParseError.incompatible_operation("or", left.return_type(), right.return_type())
        return Or(left, right)

    def visitNotValue(self, ctx):
        target = self.visit(ctx.value())
        if not Validator("not", target=target):
            ParseError.incompatible_unary_operation("not", target.return_type())
        return Not(target)

    def visitNodeValue(self, ctx):
        return Node(float(ctx.NUM().getText())).cast(self.visitCast(ctx.cast()))

    def visitArcValue(self, ctx):
        source = self.visit(ctx.source)
        target = self.visit(ctx.target)
        type_, weight = self.visit(ctx.arc())
        if source.return_type() != "node": ParseError.arc_error(source.return_type())
        if target.return_type() != "node": ParseError.arc_error(target.return_type())
        return Arc(source, target, weight, type_).cast(self.visitCast(ctx.cast()))

    def visitGraphValue(self, ctx):
        graph = Graph().cast(self.visitCast(ctx.cast()))
        for value in ctx.value():
            graph.elements.append(self.visit(value))
        return graph

    def visitNumValue(self, ctx):
        return Num(float(ctx.NUM().getText()))

    def visitIdValue(self, ctx):
        name = ctx.ID().getText()
        var = self.namespace.find_var(name)
        if var is None: ParseError.undef(name)
        return Id(name, var.type).cast(self.visitCast(ctx.cast()))

    def visitFunCallValue(self, ctx):
        fun_call = self._function_visitor().visit(ctx.funCall())
        return FunCall(fun_call).cast(self.visitCast(ctx.cast()))

    def visitLogicValue(self, ctx):
        value = True if ctx.yes else False
        return Logic(value).cast(self.visitCast(ctx.cast()))

    def visitNopeValue(self, ctx):
        return Nope()

    def visitArcPart(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            var = self.namespace.find_var(name)
            if var is not None:
                return Id(name) if var.type == "node" else ParseError.type_error(var.name, var.type, "node")
            else:
                ParseError.undef(name)
        else:
            return Node(float(ctx.NUM().getText()))

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

    def _function_visitor(self):
        return FunctionVisitior(self.block, self.namespace)
