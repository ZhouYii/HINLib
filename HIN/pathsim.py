import network, schema, base_node

def sim_score(network, node_x, node_y, lim) :
    score = 0
    for mp in network.generate_metapath(node_x, node_y, lim) :
        score += len(network.query_by_metapath(mp))
    return score


def get_sim(network, node_x, node_y, lim) :
    ''' lim defines max intermediate metapath. 
    Function returns a similarity score'''
    if network.has_node(node_x) and network.has_node(node_y) :
        xx_score = sim_score(network, node_x, node_x, lim)
        xy_score = sim_score(network, node_x, node_y, lim)
        yy_score = sim_score(network, node_y, node_y, lim)
        return 2.0*xy_score/(xx_score+yy_score)
    return -1
