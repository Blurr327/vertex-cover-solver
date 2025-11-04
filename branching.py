from basic_operations import *
from approximation_algorithms import *
from testing import *
from math import *

def update_solutions_and_edges(g, partial_solution, possible_edges, node_to_pick, node_to_discard):
   new_solution = partial_solution.union({node_to_pick}).union(g.adj[node_to_discard])
   new_possible_edges = remove_edges_containing_vertex(possible_edges, node_to_discard)
   return new_solution, new_possible_edges

def calculate_vc_lower_bound(g):
    m = len(g.edges)
    if m == 0: return 0
    n = len(g.nodes)
    _, delta = get_node_with_max_degrees(g)
    b1 = (m + 1) // delta
    b2 = (len(coupling(g))) // 2
    b3 = 0
    if (2 * n - 1) ** 2 - 8 * n > 0 :
      b3 = (2 * n - 1 - (sqrt((2 * n - 1) ** 2 - 8 * n))) // 2
    return max(b1, b2, b3)

def bf_vc_solver_v1_ext(g, edge_list, solution):
   if is_vc(g, solution):
      return solution
   u, v = edge_list.pop()
   first_case = bf_vc_solver_v1_ext(g, edge_list.copy(), solution.union({u}))
   second_case = bf_vc_solver_v1_ext(g, edge_list.copy(), solution.union({v}))
   return min(first_case, second_case, key=len)

def bf_vc_solver_v1(g):
    return bf_vc_solver_v1_ext(g, list(g.edges), set())

def bf_vc_solver_v2_ext(g, edge_list, partial_sol, best_sol):
   if is_vc(g, partial_sol):
      return min(best_sol, partial_sol, key=len)

   u, v = edge_list.pop()
   first_sol_set = partial_sol.union({u})
   second_sol_set = partial_sol.union({v})

   first_sol_min_size = calculate_vc_lower_bound(
      delete_list_nodes(g, first_sol_set)
   ) + len(first_sol_set)

   second_sol_min_size = calculate_vc_lower_bound(
      delete_list_nodes(g, second_sol_set)
   ) + len(second_sol_set)

   if first_sol_min_size < len(best_sol) :
      first_sol = bf_vc_solver_v2_ext(g, edge_list.copy(), first_sol_set, best_sol)
      best_sol = min(best_sol, first_sol, key=len)

   if second_sol_min_size < len(best_sol) :
      second_sol = bf_vc_solver_v2_ext(g, edge_list.copy(), second_sol_set, best_sol)
      best_sol = min(best_sol, second_sol, key=len)

   return best_sol

def bf_vc_solver_v2(g):
   return bf_vc_solver_v2_ext(g, list(g.edges), set(), set(g.nodes))

def bf_vc_solver_v3_ext(g, edge_list, partial_solution, best_sol):
   if is_vc(g, partial_solution):
      return min(partial_solution, best_sol, key=len)

   for u, v in edge_list:
      first_sol_set, first_edge_list = update_solutions_and_edges(g, partial_solution, edge_list, u, v)
      first_sol_min_size = calculate_vc_lower_bound(
      delete_list_nodes(g, first_sol_set)
      ) + len(first_sol_set)

      if first_sol_min_size < len(best_sol):
         first_case = bf_vc_solver_v3_ext(g, first_edge_list, first_sol_set, best_sol)
         best_sol = min(best_sol, first_case, key=len)

      second_sol_set, second_edge_list = update_solutions_and_edges(g, partial_solution, edge_list, v, u)
      second_sol_min_size = calculate_vc_lower_bound(
      delete_list_nodes(g, second_sol_set)
      ) + len(second_sol_set)

      if second_sol_min_size < len(best_sol):
         second_case = bf_vc_solver_v3_ext(g, second_edge_list, second_sol_set, best_sol)
         best_sol = min(best_sol, second_case, key=len)

   return best_sol

def bf_vc_solver_v3(g):
   return bf_vc_solver_v3_ext(g, list(g.edges), set(), coupling(g))

def bf_vc_solver_v4(g):
   node_degrees = calculate_all_degrees(g)
   cmp_func = lambda a : -node_degrees[a[0]]
   sorted_edge_list = sorted(list(g.edges), key=cmp_func)
   return bf_vc_solver_v3_ext(g, sorted_edge_list, set(), coupling(g))