from parser.grammar.SanyaScriptVisitor import SanyaScriptVisitor
from parser.parse_error import ParseError
from parser.visitors.function_visitor import FunctionVisitior
from parser.AST.values.graph import Graph
from parser.AST.values.node import Node
from parser.AST.values.arc import Arc
from parser.AST.values.num import Num
from parser.AST.values.id import Id
from parser.AST.values.fun_call import FunCall
from parser.AST.values.operations.summation import Summation
from parser.AST.values.operations.subtraction import Subtraction
from parser.AST.values.operations.multiplication import Multiplication
from parser.AST.values.operations.division import Division


class ValueVisitor(SanyaScriptVisitor):
    def __init__(self, block, namespace):
        self.namespace = namespace
        self.block = block

    def visitParenthesizedValue(self, ctx):
        return self.visit(ctx.value()).cast(self.visitCast(ctx.cast()))

    def visitDivMultValue(self, ctx);
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = ctx.operation.getText
        if operation == "*":
            return Multiplication(left, right)
        elif operation == "/":
            return Division(left, right)

    def visitSumSubstrValue(self, ctx);
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = ctx.operation.getText
        if operation == "+":
            return Summation(left, right)
        elif operation == "-":
            return Subtraction(left, right)

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
