from basic_operations import *
from testing import *
from math import *

def calculating_lower_bound(g):
   m = len(g.edges)
   n = len(g.nodes)
   _, delta = get_node_with_max_degrees(g)
   b1 = (m + 1)/delta
   b2 = 0 ## FIXME : what is b2 exactly ?
   b3 = (2*n - 1 - (sqrt((2*n - 1)**2 - 8*m))) / 2
   return max(b1, b2, b3)

def bf_vc_solver_v1_ext(g, edge_list, solution):
   if is_vc(g, solution):
      return solution

   if len(edge_list) == 0:
      return g.nodes

   branching_edge = edge_list.pop()
   first_case = bf_vc_solver_v1_ext(g, edge_list, solution.union({branching_edge[0]}))
   second_case = bf_vc_solver_v1_ext(g, edge_list, solution.union({branching_edge[0]}))
   if len(first_case) < len(second_case):
      return first_case
   else:
      return second_case

def bf_vc_solver_v1(g):
   return bf_vc_solver_v1_ext(g, list(g.edges), set())

def bf_vc_solver_v3_ext(g, edge_list, solution):
   if is_vc(g, solution):
      return solution

   if len(edge_list) == 0:
      return g.nodes

   branching_edge = edge_list.pop()

   first_solution = solution.union({branching_edge[0]}).union(g.adj[branching_edge[1]])
   first_edge_list = remove_edges_containing_vertex(edge_list, branching_edge[1])

   first_case = bf_vc_solver_v3_ext(g, first_edge_list, first_solution)

   second_solution = solution.union({branching_edge[1]}).union(g.adj[branching_edge[0]])
   second_edge_list = remove_edges_containing_vertex(edge_list, branching_edge[0])

   second_case = bf_vc_solver_v3_ext(g, second_edge_list, second_solution)

   if len(first_case) < len(second_case):
      return first_case
   else:
      return second_case

def bf_vc_solver_v3(g):
   return bf_vc_solver_v3_ext(g, list(g.edges), set())

if __name__ == "__main__":
   g = nx.Graph()
   g.add_nodes_from(["a", "b", "c", "d", "e", "f"])
   g.add_edges_from([["a", "b"], ["c", "d"], ["e", "f"]])
   print(bf_vc_solver_v3(g))
   show_solver_graph(1/2, bf_vc_solver_v1, 15)
   show_solver_graph(1/2, bf_vc_solver_v3, 25)
   # experimental_test_brute_vc_v3()


