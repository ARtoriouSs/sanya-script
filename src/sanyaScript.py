import sys
from parse.parser import Parser
from compile.compiler import Compiler


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error! Provide source and target files as argunents to this script")
        exit(1)

    code_file = sys.argv[1]
    targer_file = sys.argv[2]
    ast = Parser.parse(code_file)
    Compiler(targer_file).compile(ast)
