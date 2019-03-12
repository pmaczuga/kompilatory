import sys
import zad1_scanner
import zad2_parser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = zad2_parser.parser
    text = file.read()
    parser.parse(text, lexer=zad1_scanner.lexer)
