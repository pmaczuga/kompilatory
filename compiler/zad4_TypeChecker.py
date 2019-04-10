from zad4_SymbolTable import *
from collections import defaultdict

class NodeVisitor(object):

    def visit(self, node, table=None):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, table)


    def generic_visit(self, node, table):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):
    def __init__(self):
        self.types = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'unknown')))

        self.types['+']['int']['int'] = 'int'
        self.types['+']['float']['float'] = 'float'
        self.types['+']['int']['float'] = 'float'
        self.types['+']['float']['int'] = 'float'
        self.types['+']['vector']['int'] = 'vector'
        self.types['+']['int']['vector'] = 'vector'
        self.types['+']['vector']['float'] = 'vector'
        self.types['+']['float']['vector'] = 'vector'

        self.types['-']['int']['int'] = 'int'
        self.types['-']['float']['float'] = 'float'
        self.types['-']['int']['float'] = 'float'
        self.types['-']['float']['int'] = 'float'
        self.types['-']['vector']['int'] = 'vector'
        self.types['-']['vector']['float'] = 'vector'

        self.types['*']['int']['int'] = 'int'
        self.types['*']['float']['float'] = 'float'
        self.types['*']['int']['float'] = 'float'
        self.types['*']['float']['int'] = 'float'
        self.types['*']['vector']['int'] = 'vector'
        self.types['*']['int']['vector'] = 'vector'
        self.types['*']['vector']['float'] = 'vector'
        self.types['*']['float']['vector'] = 'vector'

        self.types['/']['int']['int'] = 'int'
        self.types['/']['float']['float'] = 'float'
        self.types['/']['int']['float'] = 'float'
        self.types['/']['float']['int'] = 'float'
        self.types['/']['vector']['int'] = 'vector'
        self.types['/']['vector']['float'] = 'vector'

        self.types['+=']['int']['int'] = 'int'
        self.types['+=']['float']['float'] = 'float'
        self.types['+=']['int']['float'] = 'float'
        self.types['+=']['float']['int'] = 'float'
        self.types['+=']['vector']['int'] = 'vector'
        self.types['+=']['vector']['float'] = 'vector'

        self.types['-=']['int']['int'] = 'int'
        self.types['-=']['float']['float'] = 'float'
        self.types['-=']['int']['float'] = 'float'
        self.types['-=']['float']['int'] = 'float'
        self.types['-=']['vector']['int'] = 'vector'
        self.types['-=']['vector']['float'] = 'vector'

        self.types['*=']['int']['int'] = 'int'
        self.types['*=']['float']['float'] = 'float'
        self.types['*=']['int']['float'] = 'float'
        self.types['*=']['float']['int'] = 'float'
        self.types['*=']['vector']['int'] = 'vector'
        self.types['*=']['vector']['float'] = 'vector'

        self.types['/=']['int']['int'] = 'int'
        self.types['/=']['float']['float'] = 'float'
        self.types['/=']['int']['float'] = 'float'
        self.types['/=']['float']['int'] = 'float'
        self.types['/=']['vector']['int'] = 'vector'
        self.types['/=']['vector']['float'] = 'vector'

        self.types['.+']['vector']['vector'] = 'vector'

        self.types['.-']['vector']['vector'] = 'vector'

        self.types['.*']['vector']['vector'] = 'vector'

        self.types['./']['vector']['vector'] = 'vector'



    def visit_Program(self, node, table):
        symbolTable = SymbolTable(None, 'global')
        self.visit(node.instructions, symbolTable)

    def visit_Instructions(self, node, table):
        for instruction in node.instructions:
            self.visit(instruction, table)

    def visit_IntNum(self, node, table):
        return 'int'

    def visit_FloatNum(self, node, table):
        return 'float'

    def visit_Variable(self, node, table):
        return 'unknown'

    def visit_Reference(self, node, table):
        


    def visit_BinExpr(self, node, table):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        # ... 
        #
 

    def visit_Variable(self, node, table):
        pass
        
