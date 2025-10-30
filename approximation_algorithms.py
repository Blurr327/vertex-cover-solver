from basic_operations import *

def coupling(g):
    G = g.copy()
    C = []
    list_of_edges = list(G.edges)

    for edge in list_of_edges:
        if edge[0] not in C and edge[1] not in C:
            C.append(edge[0])
            C.append(edge[1])
    return C

def greedy(g):
    G = g.copy()
    C = []
    list_of_edges = list(G.edges)

    while list_of_edges:
        v = get_node_with_max_degrees(G)
        G = delete_node(G, v[0])
        list_of_edges = list(G.edges)
        C.append(v[0])
    return C