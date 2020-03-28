from compile.block_compiler import BlockCompiler


class Compiler:
    def __init__(self, target):
        self.target = target

    def compile(self, ast):
        self.preload()
        BlockCompiler(open(self.target, "a")).compile(ast)

    def preload(self):
        file_ = open(self.target, "w")
        file_.flush()
        file_.write("from src.runtime import *\n")
        file_.close()
