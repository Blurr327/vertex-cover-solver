from basic_operations import *
from approximation_algorithms import *
from testing import *
from math import *

def calculating_lower_bound(g):
   m = len(g.edges)
   n = len(g.nodes)
   _, delta = get_node_with_max_degrees(g)
   b1 = (m + 1) // delta
   b2 = len(coupling(g))
   b3 = (2*n - 1 - (sqrt((2*n - 1)**2 - 8*m))) // 2
   return max(b1, b2, b3)

def bf_vc_solver_v1(g):
   if len(g.edges) == 0: return []
   branching_edge = list(g.edges)[0]
   first_case = bf_vc_solver_v1(delete_node(g, branching_edge[0]))
   second_case = bf_vc_solver_v1(delete_node(g, branching_edge[1]))
   if len(first_case) < len(second_case):
      return first_case + [branching_edge[0]]
   else :
      return second_case + [branching_edge[1]]

def bf_vc_solver_v3(g):
   if len(g.edges) == 0: return []
   branching_edge = list(g.edges)[0]
   first_case = bf_vc_solver_v3(delete_list_nodes(g, [branching_edge[0]] + list(g.adj[branching_edge[1]]))) # if we remove all the neighbors that's equivalent to not picking 1 anymore
   second_case = bf_vc_solver_v3(delete_list_nodes(g, [branching_edge[1]] + list(g.adj[branching_edge[0]])))
   if len(first_case) < len(second_case):
      return first_case + [branching_edge[0]]
   else :
      return second_case + [branching_edge[1]]

if __name__ == "__main__":
   g = nx.Graph()
   g.add_nodes_from(["a", "b", "c", "d", "e", "f"])
   g.add_edges_from([["a", "b"], ["c", "b"], ["e", "c"], ["b", "d"]])
   # show_solver_graph(1/2, bf_vc_solver_v1, 15)
   # show_solver_graph(1/2, bf_vc_solver_v3, 120)
   # experimental_test_brute_vc_v3()


