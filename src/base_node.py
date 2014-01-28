'''Basic node. Treat as virtual/abstract class. '''

class BaseNode :
    def __init__(self, attr) :
        ''' attr must correspond to a specific type in the network schema or
        the node is considered invalid. '''
        self.attr = attr

    def get_attr(self) :
        return self.attr
