from __future__ import print_function
import zad3_ast

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(zad3_ast.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)


    @addToClass(zad3_ast.IntNum)
    def printTree(self, indent=0):
        pass
        # fill in the body


    @addToClass(zad3_ast.Error)
    def printTree(self, indent=0):
        pass    
        # fill in the body


    # define printTree for other classes
    # ...

