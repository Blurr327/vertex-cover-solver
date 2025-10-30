from basic_operations import *
from approximation_algorithms import *
from testing import *
from math import *

def calculate_vc_lower_bound(g):
   m = len(g.edges)
   n = len(g.nodes)
   _, delta = get_node_with_max_degrees(g)
   b1 = (m + 1) // delta
   b2 = len(coupling(g))
   b3 = (2*n - 1 - (sqrt((2*n - 1)**2 - 8*m))) // 2
   return max(b1, b2, b3)

def bf_vc_solver_v1(g):
   if len(g.edges) == 0: return set()
   u, v = list(g.edges)[0]
   first_case = bf_vc_solver_v1(delete_node(g, u))
   second_case = bf_vc_solver_v1(delete_node(g, v))
   if len(first_case) < len(second_case):
      return first_case.union({u})
   else :
      return second_case.union({v})

def bf_vc_solver_v3(g):
   if len(g.edges) == 0: return set()
   u, v = list(g.edges)[0]
   nodes_to_add_first_case = set([u] + list(g.adj[v]))
   first_case = bf_vc_solver_v3(delete_list_nodes(g, nodes_to_add_first_case)) # if we remove all the neighbors that's equivalent to not picking 1 anymore
   nodes_to_add_second_case = set([v] + list(g.adj[u]))
   second_case = bf_vc_solver_v3(delete_list_nodes(g, nodes_to_add_second_case))
   if len(first_case) < len(second_case):
      return first_case.union(nodes_to_add_first_case)
   else :
      return second_case.union(nodes_to_add_second_case)

def bf_vc_solver_v4(g):
   if len(g.edges) == 0: return set()
   u, _ = get_node_with_max_degrees(g)
   v = list(g.adj[u])[0]
   nodes_to_add_first_case = set([u] + list(g.adj[v]))
   first_case = bf_vc_solver_v4(delete_list_nodes(g, nodes_to_add_first_case)) # if we remove all the neighbors that's equivalent to not picking 1 anymore
   nodes_to_add_second_case = set([v] + list(g.adj[u]))
   second_case = bf_vc_solver_v4(delete_list_nodes(g, nodes_to_add_second_case))
   if len(first_case) < len(second_case):
      return first_case.union(nodes_to_add_first_case)
   else :
      return second_case.union(nodes_to_add_second_case)

if __name__ == "__main__":
   g = nx.Graph()
   g.add_nodes_from(["a", "b", "c", "d", "e", "f"])
   g.add_edges_from([["a", "b"], ["c", "d"], ["e", "f"], ["b", "d"]])
   print(bf_vc_solver_v1(g))
   # show_solver_graph(1/2, bf_vc_solver_v1, 15)
   # show_solver_graph(1/2, bf_vc_solver_v3, 120)
   # experimental_test_brute_vc_v3()


