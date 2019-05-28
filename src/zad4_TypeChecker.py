from zad4_SymbolTable import *
from zad3_ast import *
from collections import defaultdict
import functools
import operator
import copy

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

class TypeChecker(NodeVisitor):
    def __init__(self):
        self.error = False

        self.types = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 'unknown')))
        self.unary_types = defaultdict(lambda: defaultdict(lambda: 'unknown'))

        self.types['+']['int']['int'] = 'int'
        self.types['+']['float']['float'] = 'float'
        self.types['+']['int']['float'] = 'float'
        self.types['+']['float']['int'] = 'float'
        self.types['+']['string']['string'] = 'string'

        self.types['-']['int']['int'] = 'int'
        self.types['-']['float']['float'] = 'float'
        self.types['-']['int']['float'] = 'float'
        self.types['-']['float']['int'] = 'float'

        self.types['*']['int']['int'] = 'int'
        self.types['*']['float']['float'] = 'float'
        self.types['*']['int']['float'] = 'float'
        self.types['*']['float']['int'] = 'float'
        self.types['*']['vector']['int'] = 'vector'
        self.types['*']['int']['vector'] = 'vector'
        self.types['*']['vector']['float'] = 'vector'
        self.types['*']['float']['vector'] = 'vector'
        self.types['*']['matrix']['matrix'] = 'matrix'
        self.types['*']['matrix']['vector'] = 'matrix'

        self.types['/']['int']['int'] = 'float'
        self.types['/']['float']['float'] = 'float'
        self.types['/']['int']['float'] = 'float'
        self.types['/']['float']['int'] = 'float'
        self.types['/']['vector']['int'] = 'vector'
        self.types['/']['vector']['float'] = 'vector'

        self.types['+=']['int']['int'] = 'int'
        self.types['+=']['float']['float'] = 'float'
        self.types['+=']['int']['float'] = 'float'
        self.types['+=']['float']['int'] = 'float'

        self.types['-=']['int']['int'] = 'int'
        self.types['-=']['float']['float'] = 'float'
        self.types['-=']['int']['float'] = 'float'
        self.types['-=']['float']['int'] = 'float'

        self.types['*=']['int']['int'] = 'int'
        self.types['*=']['float']['float'] = 'float'
        self.types['*=']['int']['float'] = 'float'
        self.types['*=']['float']['int'] = 'float'
        self.types['*=']['vector']['int'] = 'vector'
        self.types['*=']['vector']['float'] = 'vector'
        self.types['*=']['matrix']['matrix'] = 'matrix'
        self.types['*=']['matrix']['vector'] = 'matrix'

        self.types['/=']['int']['int'] = 'int'
        self.types['/=']['float']['float'] = 'float'
        self.types['/=']['int']['float'] = 'float'
        self.types['/=']['float']['int'] = 'float'
        self.types['/=']['vector']['int'] = 'vector'
        self.types['/=']['vector']['float'] = 'vector'

        self.types['.+']['vector']['vector'] = 'vector'
        self.types['.+']['matrix']['matrix'] = 'matrix'
        self.types['.+']['matrix']['int'] = 'matrix'
        self.types['.+']['matrix']['float'] = 'matrix'
        self.types['.+']['vector']['int'] = 'vector'
        self.types['.+']['vector']['float'] = 'vector'
        self.types['.+']['int']['matrix'] = 'matrix'
        self.types['.+']['float']['matrix'] = 'matrix'
        self.types['.+']['int']['vector'] = 'vector'
        self.types['.+']['float']['vector'] = 'vector'

        self.types['.-']['vector']['vector'] = 'vector'
        self.types['.-']['matrix']['matrix'] = 'matrix'
        self.types['.-']['matrix']['int'] = 'matrix'
        self.types['.-']['matrix']['float'] = 'matrix'
        self.types['.-']['vector']['int'] = 'vector'
        self.types['.-']['vector']['float'] = 'vector'
        self.types['.-']['int']['matrix'] = 'matrix'
        self.types['.-']['float']['matrix'] = 'matrix'
        self.types['.-']['int']['vector'] = 'vector'
        self.types['.-']['float']['vector'] = 'vector'

        self.types['.*']['vector']['vector'] = 'vector'
        self.types['.*']['matrix']['matrix'] = 'matrix'
        self.types['.*']['matrix']['int'] = 'matrix'
        self.types['.*']['matrix']['float'] = 'matrix'
        self.types['.*']['vector']['int'] = 'vector'
        self.types['.*']['vector']['float'] = 'vector'
        self.types['.*']['int']['matrix'] = 'matrix'
        self.types['.*']['float']['matrix'] = 'matrix'
        self.types['.*']['int']['vector'] = 'vector'
        self.types['.*']['float']['vector'] = 'vector'

        self.types['./']['vector']['vector'] = 'vector'
        self.types['./']['matrix']['matrix'] = 'matrix'
        self.types['./']['matrix']['int'] = 'matrix'
        self.types['./']['matrix']['float'] = 'matrix'
        self.types['./']['vector']['int'] = 'vector'
        self.types['./']['vector']['float'] = 'vector'
        self.types['./']['int']['matrix'] = 'matrix'
        self.types['./']['float']['matrix'] = 'matrix'
        self.types['./']['int']['vector'] = 'vector'
        self.types['./']['float']['vector'] = 'vector'

        self.types['==']['int']['int'] = 'boolean'
        self.types['==']['float']['float'] = 'boolean'
        self.types['==']['int']['float'] = 'boolean'
        self.types['==']['float']['int'] = 'boolean'
        self.types['==']['string']['string'] = 'boolean'
        self.types['==']['vector']['vector'] = 'boolean'
        self.types['==']['matrix']['matrix'] = 'boolean'

        self.types['!=']['int']['int'] = 'boolean'
        self.types['!=']['float']['float'] = 'boolean'
        self.types['!=']['int']['float'] = 'boolean'
        self.types['!=']['float']['int'] = 'boolean'
        self.types['!=']['string']['string'] = 'boolean'
        self.types['!=']['vector']['vector'] = 'boolean'
        self.types['!=']['matrix']['matrix'] = 'boolean'

        self.types['>']['int']['int'] = 'boolean'
        self.types['>']['float']['float'] = 'boolean'
        self.types['>']['int']['float'] = 'boolean'
        self.types['>']['float']['int'] = 'boolean'
        self.types['>']['string']['string'] = 'boolean'
        self.types['>']['vector']['vector'] = 'boolean'
        self.types['>']['matrix']['matrix'] = 'boolean'

        self.types['<']['int']['int'] = 'boolean'
        self.types['<']['float']['float'] = 'boolean'
        self.types['<']['int']['float'] = 'boolean'
        self.types['<']['float']['int'] = 'boolean'
        self.types['<']['string']['string'] = 'boolean'
        self.types['<']['vector']['vector'] = 'boolean'
        self.types['<']['matrix']['matrix'] = 'boolean'

        self.types['>=']['int']['int'] = 'boolean'
        self.types['>=']['float']['float'] = 'boolean'
        self.types['>=']['int']['float'] = 'boolean'
        self.types['>=']['float']['int'] = 'boolean'
        self.types['>=']['string']['string'] = 'boolean'
        self.types['>=']['vector']['vector'] = 'boolean'
        self.types['>=']['matrix']['matrix'] = 'boolean'

        self.types['<=']['int']['int'] = 'boolean'
        self.types['<=']['float']['float'] = 'boolean'
        self.types['<=']['int']['float'] = 'boolean'
        self.types['<=']['float']['int'] = 'boolean'
        self.types['<=']['string']['string'] = 'boolean'
        self.types['<=']['vector']['vector'] = 'boolean'
        self.types['<=']['matrix']['matrix'] = 'boolean'

        self.unary_types['NEGATE']['int'] = 'int'
        self.unary_types['NEGATE']['float'] = 'float'
        self.unary_types['NEGATE']['vector'] = 'vector'
        self.unary_types['NEGATE']['matrix'] = 'matrix'

        self.unary_types['TRANSPOSE']['vector'] = 'matrix'
        self.unary_types['TRANSPOSE']['matrix'] = 'matrix'

    def handle_error(self, message):
        self.error = True
        print(message)

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
        symbol = table.get(node.name)
        if symbol:
            return symbol.type
        else:
            self.handle_error('Line {}: {} is used but not declared'.format(node.line, node.name))
            return 'unknown'

    def visit_Reference(self, node, table):
        symbol = table.get(node.variable.name)
        types = [self.visit(i, table) for i in node.indexes]

        for t in types:
            if t != 'unknown' and t != 'int':
                self.handle_error('Line {}: index is not integer'.format(node.line))
                return 'unknown'

        if not symbol:
            self.handle_error('Line {}: {} is used but not declared'.format(node.line, node.variable.name))
            return 'unknown'
        if symbol.type == 'unknown':
            return 'unknown'
        elif symbol.type != 'vector' and symbol.type != 'matrix':
            self.handle_error('Line {}: Reference to: {}'.format(node.line, symbol.type))
            return 'unknown'

        if len(node.indexes) > 2:
            self.handle_error('Line {}: {} reference to two many indexes in {}'.format(node.line, node.variable.name, symbol.type))
        if symbol.type == 'vector' and len(node.indexes) != 1:
            self.handle_error('Line {}: {} reference to two many indexes in {}'.format(node.line, node.variable.name, symbol.type))

        # TODO - try to check type somehow
        return 'float'

    def get_matrix_vector_dims(self, matrix, table):
        dims = None
        matrix = copy.deepcopy(matrix)
        if isinstance(matrix, Variable):
            matrix = table.get(matrix.name)
            if not matrix:
                return None
            matrix = matrix.value
        if isinstance(matrix, Vector):
            dims = matrix.int_dims()
        elif isinstance(matrix, MatrixInit) and matrix.int_dims():
            dims = matrix.int_dims()
        return dims

    def visit_BinExpr(self, node, table):
        left_type = self.visit(node.left, table)
        right_type = self.visit(node.right, table)
        op = node.op
        if left_type == 'unknown' or right_type == 'unknown':
            return 'unknown'
        return_type = self.types[op][left_type][right_type]
        if return_type == 'unknown':
            self.handle_error('Line {}: Operation {} unsupported between types: {} and {}'.format(node.line, op, left_type, right_type))
            return 'unknown'

        # check if opreration can be performed on matrixes (vectors) with this dimensions
        if (right_type == 'matrix' or right_type == 'vector') and (left_type == 'matrix' or left_type == 'vector'):
            right = node.right
            left = node.left
            right_dims = self.get_matrix_vector_dims(right, table)
            left_dims = self.get_matrix_vector_dims(left, table)
            if op in ('.+', '.-', '.*', './'):
                if right_dims and left_dims:
                    if right_dims != left_dims:
                        self.handle_error('Line {}: Elementwise operation between arrays of wrong dimensions: {} and {}'.format(node.line, left_dims, right_dims))
                        return 'unknown'
            if op == '*':
                if right_dims and left_dims:
                    if left_dims[1] != right_dims[0]:
                        self.handle_error('Line {}: Multiplication between matrixes of wrong dimensions: {} and {}'.format(node.line, left_dims, right_dims))
                        return 'unknown'

        return return_type

    def visit_Assignment(self, node ,table):
        right_type = self.visit(node.right, table)
        if isinstance(node.left, Reference):
            self.visit(node.left, table)
            if right_type != 'int' and right_type != 'float' and right_type != 'unkown':
                self.handle_error('Line {}: Assignment to reference {} of wrong type: {}'.format(node.line, node.left.variable.name, right_type))
        elif isinstance(node.left, Variable):
            table.put(node.left.name ,VariableSymbol(node.left.name, right_type, node.right))

    def visit_AssignmentAndExpr(self, node, table):
        left_type = self.visit(node.left, table)
        right_type = self.visit(node.right, table)
        ttype = self.types[node.op][node.left][node.right]
        if ttype == 'unkown':
            self.handle_error('Line {}: Operation {} unsupported between types: {} and {}'.format(node.line, op, left_type, right_type))
            return
        left_dims = self.get_matrix_vector_dims(node.left, table)
        right_dims = self.get_matrix_vector_dims(node.right, table)
        if node.op == '*=':
            if (left_type == 'matrix' and (right_type == 'matrix' or right_type == 'vector')):
                if right_dims and left_dims:
                    if left_dims[1] != right_dims[0]:
                        self.handle_error('Line {}: Multiplication between matrixes of wrong dimensions: {} and {}'.format(node.line, left_dims, right_dims))
                        return

    def visit_Condition(self, node ,table):
        left_type = self.visit(node.left, table)
        right_type = self.visit(node.right, table)
        op = node.op
        if left_type == 'unknown' or right_type == 'unknown':
            return 'boolean'
        return_type = self.types[op][left_type][right_type]
        if return_type == 'unknown':
            self.handle_error('Line {}: Operation {} unsupported between types: {} and {}'.format(node.line, op, left_type, right_type))
        return 'boolean'

    def visit_UnaryExpr(self, node ,table):
        unary_type = self.visit(node.arg, table)
        op = node.op
        if unary_type == 'unknown':
            return 'unknown'
        return_type = self.unary_types[op][unary_type]
        if return_type == 'unknown':
            self.handle_error('Line {}: Operation {} unsupported on type {}'.format(node.line, op, unary_type))
        return return_type

    def visit_For(self, node ,table):
        symbol_table = SymbolTable(table, 'for')
        range_type = self.visit(node.range_, table)
        symbol_table.put(node.variable.name, VariableSymbol(node.variable.name, range_type, None))
        self.visit(node.instruction, symbol_table)

    def visit_While(self, node ,table):
        symbol_table = SymbolTable(table, 'while')
        self.visit(node.condition, table)
        self.visit(node.instruction, symbol_table)

    def visit_If(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction, table)
        if node.else_instruction:
            self.visit(node.else_instruction, table)

    def visit_Range(self, node, table):
        start_type = self.visit(node.start, table)
        end_type = self.visit(node.end, table)
        if start_type == 'unknown' or end_type == 'unknown':
            return 'unknown'
        elif start_type != 'int' or end_type != 'int':
            self.handle_error('Line {}: Range of unsupported types: {} and {}'.format(node.line, start_type, end_type))
            return 'unknown'
        return 'int'

    def visit_Return(self, node, table):
        if node.value:
            return self.visit(node.value, table)

    def visit_Print(self, node, table):
        for expr in node.expressions:
            self.visit(expr, table)

    def visit_Continue(self, node, table):
        if table.name == 'global':
            self.handle_error('Line {}: Continue from global scope'.format(node.line))

    def visit_Break(self, node, table):
        if table.name == 'global':
            self.handle_error('Line {}: Break from global scope'.format(node.line))

    def visit_Vector(self, node, table):
        coor_types = [self.visit(t, table) for t in node.coordinates]
        if self.types.__contains__('unknown'):
            return 'unknown'
        if not len(set(coor_types)) == 1:
            self.handle_error('Line {}: Vector initialization with different types'.format(node.line)) 
            return 'unknown'
        coor_type = coor_types[0]
        if coor_type == 'int' or coor_type == 'float':
            return 'vector'
        if coor_type == 'vector':
            if not len(set([len(l.coordinates) for l in node.coordinates])) == 1:
                self.handle_error('Line {}: Matrix initialization with vectors of different sizes'.format(node.line)) 
                return 'unknown'
            return 'matrix'
        self.handle_error('Line {}: Vector initialization with illegal type: {}'.format(node.line, coor_type)) 
        return 'unknown'

    def visit_MatrixInit(self, node, table):
        dim1_type = self.visit(node.dim_1, table)
        dim2_type = dim1_type
        if node.dim_2:
            dim2_type = self.visit(node.dim_2, table)
        if dim1_type != 'int':
            self.handle_error('Line {}: Matrix initialization with illegal dims type: {}'.format(node.line, dim1_type)) 
            return 'unknown'
        if dim2_type != 'int':
            self.handle_error('Line {}: Matrix initialization with illegal dims type: {}'.format(node.line, dim2_type)) 
            return 'unknown'
        return 'matrix'

    def visit_Eye(self, node, table):
        return self.visit_MatrixInit(node, table)

    def visit_Zeros(self, node, table):
        return self.visit_MatrixInit(node, table)

    def visit_Ones(self, node, table):
        return self.visit_MatrixInit(node, table)

    def visit_String(self, node, table):
        return 'string'


        
