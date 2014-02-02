''' HIN '''
import sys
class HetNetwork :
    def __init__(self, schema=None) :
        if schema == None :
            print "Error : Need schema"
            sys.exit()
        self.schema = schema
        self.nodes = list()
        #2 layer hash is also good
        self.edges = dict()

    def add_node(self, node) :
        node_attr = node.get_attr()
        if self.schema.has_attr(node_attr) :
            self.nodes.append(node)
    def has_node(self, node) :
        return node in self.nodes 

    def rm_node(self, node) :
        if node in self.nodes :
            self.nodes.remove(node)

    def verify_relationship(self, start, end) :
        start_attr = start.get_attr()
        end_attr = end.get_attr()
        return self.schema.has_relation(start_attr, end_attr)

    def add_edge(self, start, end) :
        ''' Start and end are the respective nodes '''
        edge = (start, end)
        if start in self.nodes and end in self.nodes :
            if verify_relationship(self, start, end) :
                if not self.edges.has_key(start.get_attr()) :
                    self.edges[start.get_attr()] = dict()
                self.edges[start.get_attr()][end.get_attr()] = edge

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

    def get_edges(self, filter_fxn) :
        return self.edges

    def query_by_metapath(self, metapath) :
        ''' path is a list of nodes
        metapath is a list of attribute keys 
        function returns all paths which match metapath'''
        def metapath_filter(self, path, metapath) :
            acc = []
            node = path[-1]
            if len(metapath) == 0:
                return acc
            next_attr = metapath[0]
            for endpt in self.edges[node].values() :
                if next_attr == endpt.get_attr():
                    acc.append(path.copy().append(endpt))
            return acc

        ret = []
        for node in self.nodes :
            ret.append([node])
        while len(ret) > 0 and len(metapath) > 0 :
            ret = metapath_filter(self, ret, metapath)
            metapath = metapath[1:]
        return ret

    def generate_metapath(self, node_x, node_y, lim) :
        if lim == 1 and node_x.get_attr() == node_y.get_attr() :
            return [node_x.get_attr()]
        if lim <= 1 :
            return []
        ret = []
        for endpt in self.edges[node_x].get_values() :
            tmp = generate_metapath(self, endpt, node_y, lim-1)
            for metapath in tmp :
                ret.append([endpt.get_attr()].extend(metapath))
        return set(ret)
