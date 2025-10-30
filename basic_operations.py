import networkx as nx
import random

def delete_node(g, v):
    G = g.copy()
    list_nodes = list(G.nodes)
    for node in list_nodes:
        for neighbor in list(G.adj[node]):
            if (node == v or neighbor == v):
                G.remove_edge(node, neighbor)

    G.remove_node(v)
    return G

def delete_list_nodes(g, list_som):
    G = g.copy()
    for som in set(list_som):
        G = delete_node(G, som)
    return G

def calculate_all_degrees(g):
  list_of_nodes = list(g.nodes)
  node_degrees = {}
  for node in list_of_nodes:
      node_degrees[node] = 0
  for node in list_of_nodes:
    for _ in g.adj[node]:
      node_degrees[node] += 1
  return node_degrees

def get_node_with_max_degrees(g):
    list_of_nodes = list(g.nodes)
    degrees = calculate_all_degrees(g)
    max = list_of_nodes[0]
    for node in list_of_nodes:
        if degrees[max] < degrees[node]:
            max = node
    return max, degrees[max]

def generate_random_graph(n, p):
    g = nx.Graph()
    for i in range(n):
        g.add_node(i)

    for i in range(n):
        for j in range(n):
            if i != j and random.choices([0, 1], [1-p, p])[0] :
                g.add_edge(i, j)
    return g

def remove_edges_containing_vertex(edges_list, vertex):
   res = edges_list.copy()
   for edge in edges_list:
      if vertex in edge:
         res.remove(edge)
   return res

# FIXME : might not need this
def is_vc(g, c):
    G = delete_list_nodes(g, c)
    return len(G.edges) == 0