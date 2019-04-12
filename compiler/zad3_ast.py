class Node(object):
    def __init__():
        self.line = 0
        self.column = 0

class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions

class Instructions(Node):
    def __init__(self, instructions = []):
        self.instructions = instructions

class Number(Node):
    def __init__(self, value):
        self.value = value

class IntNum(Number):
    pass

class FloatNum(Number):
    pass

class Variable(Node):
    def __init__(self, name):
        self.name = name

class Reference(Node):
    def __init__(self, variable, indexes):
        self.variable = variable
        self.indexes = indexes

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Assignment(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Condition(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnaryExpr(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

class For(Node):
    def __init__(self, variable, range_, instruction):
        self.variable = variable
        self.range_ = range_
        self.instruction = instruction

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class If(Node):
    def __init__(self, condition, instruction, else_instruction=None):
        self.condition = condition
        self.instruction = instruction
        self.else_instruction = else_instruction

class Range(Node):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Return(Node):
    def __init__(self, value):
        self.value = value

class Print(Node):
    def __init__(self, expressions):
        self.expressions = expressions

class Continue(Node):
    def __init__(self):
        pass

class Break(Node):
    def __init__(self):
        pass

class Vector(Node):
    def __init__(self, coordinates):
        self.coordinates = coordinates

class MatrixInit(Node):
    def __init__(self, dim_1, dim_2=None):
        self.dim_1 = dim_1
        self.dim_2 = dim_2

class Eye(MatrixInit):
    pass

class Zeros(MatrixInit):
    pass

class Ones(MatrixInit):
    pass

class String(Node):
    def __init__(self, value):
        self.value = value


class Error(Node):
    def __init__(self):
        pass
      