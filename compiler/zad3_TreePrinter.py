from __future__ import print_function
import zad3_ast

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @classmethod
    def printIndented(cls, string, level):
        print ("|  " * level + string)

    @addToClass(zad3_ast.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(zad3_ast.Program)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    @addToClass(zad3_ast.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree(indent)

    @addToClass(zad3_ast.IntNum)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)

    @addToClass(zad3_ast.FloatNum)
    def printTree(self, indent=0):
        TreePrinter.printIndented(str(self.value), indent)

    @addToClass(zad3_ast.Variable)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.name, indent)

    @addToClass(zad3_ast.Reference)
    def printTree(self, indent=0):
        TreePrinter.printIndented("REF", indent)
        self.variable.printTree(indent + 1)
        for index in self.indexes:
            index.printTree(indent + 1)

    @addToClass(zad3_ast.BinExpr)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(zad3_ast.Assignment)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(zad3_ast.Condition)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(zad3_ast.UnaryExpr)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.op, indent)
        self.arg.printTree(indent + 1)

    @addToClass(zad3_ast.For)
    def printTree(self, indent=0):
        TreePrinter.printIndented("FOR", indent)
        self.variable.printTree(indent + 1)
        self.range_.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(zad3_ast.While)
    def printTree(self, indent=0):
        TreePrinter.printIndented("WHILE", indent)
        self.condition.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(zad3_ast.If)
    def printTree(self, indent=0):
        TreePrinter.printIndented("IF", indent)
        self.condition.printTree(indent + 1)
        TreePrinter.printIndented("THEN", indent)
        self.instruction.printTree(indent + 1)
        if self.else_instruction:
            TreePrinter.printIndented("ELSE", indent)
            self.else_instruction.printTree(indent + 1)

    @addToClass(zad3_ast.Range)
    def printTree(self, indent=0):
        TreePrinter.printIndented("RANGE", indent)
        self.start.printTree(indent + 1)
        self.end.printTree(indent + 1)

    @addToClass(zad3_ast.Return)
    def printTree(self, indent=0):
        TreePrinter.printIndented("RETURN", indent)
        if self.value:
            self.value.printTree(indent + 1)

    @addToClass(zad3_ast.Print)
    def printTree(self, indent=0):
        TreePrinter.printIndented("PRINT", indent)
        for expression in self.expressions:
            expression.printTree(indent + 1)

    @addToClass(zad3_ast.Continue)
    def printTree(self, indent=0):
        TreePrinter.printIndented("CONTINUE", indent)

    @addToClass(zad3_ast.Break)
    def printTree(self, indent=0):
        TreePrinter.printIndented("BREAK", indent)

    @addToClass(zad3_ast.Vector)
    def printTree(self, indent=0):
        TreePrinter.printIndented("VECTOR", indent)
        for coordinate in self.coordinates:
            coordinate.printTree(indent + 1)

    @addToClass(zad3_ast.Eye)
    def printTree(self, indent=0):
        TreePrinter.printIndented("EYE", indent)
        self.dim_1.printTree(indent + 1)
        if self.dim_2:
            self.dim_2.printTree(indent + 1)

    @addToClass(zad3_ast.Zeros)
    def printTree(self, indent=0):
        TreePrinter.printIndented("ZEROS", indent)
        self.dim_1.printTree(indent + 1)
        if self.dim_2:
            self.dim_2.printTree(indent + 1)

    @addToClass(zad3_ast.Ones)
    def printTree(self, indent=0):
        TreePrinter.printIndented("ONES", indent)
        self.dim_1.printTree(indent + 1)
        if self.dim_2:
            self.dim_2.printTree(indent + 1)

    @addToClass(zad3_ast.String)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.value, indent)

    @addToClass(zad3_ast.Error)
    def printTree(self, indent=0):
        pass    
        # fill in the body
