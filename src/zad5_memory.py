

class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.symbols = dict()

    def has_key(self, name):  # variable name
        return self.symbols.__contains__(name)

    def get(self, name):         # gets from memory current value of variable <name>
        return self.symbols[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.symbols[name] = value


class MemoryStack:
                                                                             
    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        if memory and not isinstance(memory, Memory):
            raise ValueError("Memory argument not instacne of Memory")
        self.stack = list()
        if memory:
            self.stack.append(memory)
        else:
            self.stack.append(Memory("global"))

    def get(self, name):             # gets from memory stack current value of variable <name>
        for memory in self.stack[::-1]:
            if memory.has_key(name):
                return memory.get(name)
        raise KeyError(name)

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stack[-1].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        for memory in self.stack[::-1]:
            if memory.has_key(name):
                memory.put(name, value)
                return
        raise KeyError(name)

    def push(self, memory): # pushes memory <memory> onto the stack
        if not isinstance(memory, Memory):
            raise ValueError("Memory argument not instacne of Memory")
        self.stack.append(memory)

    def pop(self):          # pops the top memory from the stack
        return self.stack.pop()


