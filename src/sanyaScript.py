import sys

from parser.parser import Parser
from compiler.compiler import Compiler


BUILTINS_FILE = "src/runtime/builtins_signatures.sanya"

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error! Provide source and target files as argunents to this script")
        exit(1)

    code_file = sys.argv[1]
    targer_file = sys.argv[2]
    ast = Parser(code_file, [BUILTINS_FILE]).parse()
    Compiler(targer_file).compile(ast)
