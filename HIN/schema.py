''' Network Schema'''

class NetworkSchema:
    ''' For now, attr are represented as unique string '''
    def __init__(self, attr={}, relation={}):
        ''' Construction for network schema takes initial list of attribute 
        and relation types'''
        self.attr = set(attr)
        self.relation = set(relation)

    def add_attr(self, key) :
        self.attr.add(key)

    def add_relation(self, start, end) :
        if start in self.attr and end in self.attr :
            self.relation.add((start, end))

    def rm_attr(self, key) :
        if key in self.attr :
            self.attr.discard(key)
            #Remove invalid relationship types
            inv_list = []
            for r in self.relation :
                if key in r:
                    inv_list.append(r)

            for invalid in inv_list:
                self.relation.discard(invalid)

    def rm_relation(self, start, end) :
        self.relation.discard((start,end))

    def has_attr(self, key) :
        return key in self.attr

    def has_relation(self, start, end) :
        return (start, end) in self.relation

