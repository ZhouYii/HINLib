''' Network Schema'''

class NetworkSchema:
    ''' For now, attr are represented as unique string '''
    def __init__(self, attr={}, relation={}):
        ''' Construction for network schema takes initial list of attribute 
        and relation types'''
        self.attr = attr
        self.relation = relation

    def add_attr(self, key) :
        self.attr.add(key)

    def add_relation(self, start, end) :
        if start in self.attr and end in self.attr :
            self.relations.add(tuple(start, end))

    def rm_attr(self, key) :
        if key in self.attr :
            self.attr.discard(key)
            #Remove invalid relationship types
            for r in self.relation :
                if key in r:
                    self.relation.discard(r)

    def rm_relation(self, start, end) :
        self.relation.discard((start,end))

    def has_attr(self, key) :
        return key in self.attr

    def has_relation(self, start, end) :
        return (start, end) in self.relation

