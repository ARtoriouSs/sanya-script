import os

from compiler.block_compiler import BlockCompiler


class Compiler:
    def __init__(self, target):
        self.target = target

    def compile(self, ast):
        self.preload()
        BlockCompiler(open(self.target, "a")).compile(ast)
        self._make_executable()

    def preload(self):
        file_ = open(self.target, "w")
        file_.flush()
        file_.write("#!/usr/bin/python3\n")
        file_.write("from sanya_script_runtime import *\n")
        file_.close()

    def _make_executable(self):
        os.system(f"chmod +x {self.target}")
