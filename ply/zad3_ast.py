class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name, index_1 = None, index_2 = None):
        self.name = name
        self.index_1 = index_1
        self.index_2 = index_2

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnaryExpr(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

class For(Node):
    def __init__(self, variable, my_range, instruction):
        self.variable = variable
        self.my_range = my_range
        self.instruction = instruction

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class If(Node):
    def __init__(self, condition, instruction, else_instruction = None):
        self.condition = condition
        self.instruction = instruction
        self.else_instruction = else_instruction

class My_range(Node):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Return(Node):
    def __init__(self, value):
        self.value = value

class Print(Node):
    def __init__(self, value):
        self.value = value

class Continue(Node):
    def __init__(self):
        pass

class Break(Node):
    def __init__(self):
        pass

class Vector(Node):
    def __init__(self, coordinates):
        self.coordinates = coordinates

class Matrix(Node):
    def __init__(self, vectors):
        self.vectors = vectors

class String(Node):
    def __init__(self, value):
        self.value = value

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
      