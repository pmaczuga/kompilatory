
class ReturnValueException(Exception):

    def __init__(self,value=None):
        self.value = value
        
class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass
