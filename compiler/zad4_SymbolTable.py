class Symbol(object):
    pass

class VariableSymbol(Symbol):
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.symbols = {}
        self.parent = parent
        self.name = name

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if self.symbols.__contains__(name):
            return self.symbols[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        pass
    #

    def popScope(self):
        pass
    #


