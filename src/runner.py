import sys

from parser.parser import Parser
from analyzer.analyzer import Analyzer
from compiler.compiler import Compiler


BUILTINS_FILE = "src/runtime/builtins_signatures.sanya"

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Error! Provide source and target files as argunents")
        exit(1)

    code_file = sys.argv[1]
    target_file = sys.argv[2]
    directory = sys.argv[3]

    builtins = directory + "/" + BUILTINS_FILE

    ast = Parser(code_file, [builtins]).parse()
    if Analyzer().validate(ast):
        Compiler(target_file).compile(ast)
