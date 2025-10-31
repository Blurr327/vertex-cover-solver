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
    b3 = (2 * n - 1 - (sqrt((2 * n - 1) ** 2 - 8 * m))) // 2
    return max(b1, b2, b3)


def bf_vc_solver_v1_ext(g, edge_list, solution):
   if is_vc(g, solution):
      # DEBUG
   #   print("this is a solution", solution)
      return solution
   u, v = edge_list.pop()
   #DEBUG
#  print("solution",solution)
#  print("edge list", edge_list, "branching edge", (u, v))
   first_case = bf_vc_solver_v1_ext(g, edge_list.copy(), solution.union({u}))
   second_case = bf_vc_solver_v1_ext(g, edge_list.copy(), solution.union({v}))
   return min(first_case, second_case, key=len)


def bf_vc_solver_v1(g):
    return bf_vc_solver_v1_ext(g, list(g.edges), set())

def bf_vc_solver_v3_ext(g, edge_list, solution):
   if is_vc(g, solution):
      return solution

   best = set(g.nodes)
   for u, v in edge_list:
      first_solution = solution.union({u}).union(g.adj[v])
      first_edge_list = remove_edges_containing_vertex(edge_list, v)

      first_case = bf_vc_solver_v3_ext(g, first_edge_list, first_solution)

      second_solution = solution.union({v}).union(g.adj[u])
      second_edge_list = remove_edges_containing_vertex(edge_list, u)

      second_case = bf_vc_solver_v3_ext(g, second_edge_list, second_solution)

      best = min(best, first_case, second_case, key=len)

   return best

def bf_vc_solver_v3(g):
   return bf_vc_solver_v3_ext(g, list(g.edges), set())



if __name__ == "__main__":
    g = nx.Graph()
    g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7])
    g.add_edges_from(
        [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 3), (1, 5), (1, 6), (1, 7), (1, 4), (2, 3), (2, 5), (2, 6), (2, 7), (2, 4), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6), (4, 7), (5, 7), (5, 6), (6, 7)]
    )
    print(bf_vc_solver_v3(g))
    # show_solver_graph(1/2, bf_vc_solver_v1, 15)
    # show_solver_graph(1/2, bf_vc_solver_v3, 120)
    # experimental_test_brute_vc_v3()
