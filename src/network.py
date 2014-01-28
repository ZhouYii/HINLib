''' HIN '''
import sys
class HetNetwork :
    def __init__(self, schema=None) :
        if schema == None :
            print "Error : Need schema"
            sys.exit()
        self.schema = schema
        self.attr_dict = dict()
        self.nodes = list()
        #2 layer hash is also good
        self.edges = dict()

    def add_node(self, node) :
        node_attr = node.get_attr()
        if self.schema.has_attr(node_attr) :
            self.nodes.append(node)

            if self.attr_dict.has_key(node_attr) :
                self.attr_dict[node_attr].append(node_attr)
            else :
                self.attr_dict[node_attr] = [node_attr]

    def rm_node(self, node) :
        if node in self.nodes :
            self.nodes.remove(node)
        if self.attr_dict.has_key(node.get_attr()) :
            attr_list = self.attr_dict[node.get_attr()]
            if attr_list.count(node) > 0 :
                attr_list.remove(node)

    def verify_relationship(self, start, end) :
        start_attr = start.get_attr()
        end_attr = end.get_attr()
        return self.schema.has_relation(start_attr, end_attr)

    def add_edge(self, start, end) :
        ''' Start and end are the respective nodes '''
        edge = (start, end)
        if start in self.nodes and end in self.nodes :
            if verify_relationship(self, start, end) :
                if self.edges.has_key(start.get_attr()) :
                    self.edges[start.get_attr()].append(edge)
                else :
                    self.edges[start.get_attr()] = [edge]

    def rm_edge(self, edge) :
        ''' Assumes for now that edge is (start, end) since there is no
        tuple-specific interface '''
        start_attr = edge[0].get_attr()
        if self.edges.has_key(start_attr) :
            if self.edges[start_attr].count(edge) > 0 :
                self.edges[start_attr].remove(edge)

    #The extraction method for nodes. 
    def get_nodes(self, filter_fxn) :
        ''' Maps filter_fxn over node list, returning all that satisfy the
        filter. '''
        return filter(filter_fxn, self.nodes)


