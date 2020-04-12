from .types.num import Num


def scan():
    return Num(input())

def print(obj):
    obj.print()

def println(obj):
    obj.println()

def source(arc):
    return arc.source

def target(arc):
    return arc.target

def weight(arc):
    return Num(arc.weight)

def value(node):
    return Num(node.value)

def arcs(graph):
    return list(graph.arcs)

def nodes(graph):
    return list(graph.nodes)
