import sys
import zad1_scanner
import zad2_parser
from zad3_TreePrinter import TreePrinter
from zad4_TypeChecker import TypeChecker
from zad5_interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = zad2_parser.parser
    text = file.read()
    ast = parser.parse(text, lexer=zad1_scanner.lexer)
    if ast:
        ast.printTree()

        typeChecker = TypeChecker()   
        typeChecker.visit(ast)

        if not typeChecker.error:
            print("\n\nOUTPUT:\n")
            ast.accept(Interpreter())
