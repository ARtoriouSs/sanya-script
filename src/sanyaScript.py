import sys
from parse.parser import Parser
from compile.compiler import Compiler


if __name__ == '__main__':
    code_file = sys.argv[1]
    targer_file = sys.argv[2]
    ast = Parser().parse(code_file)
    Compiler(targer_file).compile(ast)
