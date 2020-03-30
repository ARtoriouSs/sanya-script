from compiler.block_compiler import BlockCompiler


class Compiler:
    def __init__(self, target):
        self.target = target

    def compile(self, ast):
        self.preload()
        BlockCompiler(open(self.target, "a")).compile(ast)

    def preload(self):
        file_ = open(self.target, "w")
        file_.flush()
        self.import_runtime(file_)
        file_.close()

    def import_runtime(self, file_):
        file_.write("from src.runtime.types.num import Num\n")
        file_.write("from src.runtime.types.node import Node\n")
        file_.write("from src.runtime.types.arc import Arc\n")
        file_.write("from src.runtime.types.graph import Graph\n")
