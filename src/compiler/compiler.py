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
        self._add_interpreter(file_)
        self._import_runtime(file_)
        file_.close()

    def _add_interpreter(self, file_):
        file_.write("#!/usr/bin/python3\n")

    def _import_runtime(self, file_):
        file_.write("from src.runtime.types.num import Num\n")
        file_.write("from src.runtime.types.node import Node\n")
        file_.write("from src.runtime.types.arc import Arc\n")
        file_.write("from src.runtime.types.graph import Graph\n")
        file_.write("from src.runtime.types.logic import Logic\n")
        file_.write("from src.runtime.types.nope import Nope\n")
        file_.write("from src.runtime.builtins import *\n")

    def _make_executable(self):
        os.system(f"chmod +x {self.target}")
