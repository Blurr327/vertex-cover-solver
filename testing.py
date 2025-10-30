import matplotlib.pyplot as plt
from basic_operations import *
from approximation_algorithms import *
from time import time
import numpy as np
from math import *
import networkx as nx

def test_vc_solver(p, vc_solver, max_size, nb_of_points=50, tests_per_size=10):
   x_points = []
   y_points = []
   for n in range(max_size//nb_of_points, max_size+1, max_size//nb_of_points):
      sum_of_durations = 0
      for _ in range(tests_per_size):
         g = generate_random_graph(n, p)
         start = time()
         vc_solver(g)
         duration = time() - start
         sum_of_durations += duration
      average_duration = sum_of_durations / tests_per_size
      x_points.append(n)
      y_points.append(average_duration)
   return np.array(x_points), np.array(y_points)

def save_graph(x_points, y_points, x_label="Size of the graph (number of vertices)", y_label="", filename="bruh"):
   plt.clf()
   plt.plot(x_points, y_points, marker='o')
   plt.xlabel(x_label)
   plt.ylabel(y_label)
   plt.savefig(filename)

def save_solver_graph(p, vc_solver, max_size, f="bruh"):
   x_points, y_points = test_vc_solver(p, vc_solver, max_size)
   save_graph(x_points, y_points, y_label="Time in seconds", filename=f)

def save_solver_log_graph(p, vc_solver, max_size, f="bruh"):
   x_points, y_points = test_vc_solver(p, vc_solver, max_size)
   save_graph(x_points, [log(t) for t in y_points], y_label="log of time in seconds", filename=f)

def parse_graph(name_of_file):
   f = open(name_of_file)
   data = f.read().split("\n")
   line_nbr_for_nb_of_nodes = 1
   line_nbr_for_start_of_node_list = line_nbr_for_nb_of_nodes + 2
   number_of_nodes = int(data[line_nbr_for_nb_of_nodes])
   line_nbr_for_nb_of_edges = line_nbr_for_start_of_node_list + number_of_nodes + 1
   line_nbr_for_start_of_edge_list = line_nbr_for_nb_of_edges + 2
   number_of_edges = int(data[line_nbr_for_nb_of_edges])

   g = nx.Graph()
   g.add_nodes_from(data[
      line_nbr_for_start_of_node_list :
      line_nbr_for_start_of_node_list + number_of_nodes
        ])
   list_of_edges = data[
      line_nbr_for_start_of_edge_list :
      line_nbr_for_start_of_edge_list + number_of_edges
      ]
   for edge in list_of_edges :
      g.add_edge(*edge.split(" "))
   return g

# if __name__ == "__main__":
   # Finding Nmax
   # g = generate_random_graph(200, 0.5)
   # greedy(g)

   # Nmax = 100
   # p = 0.3
   # save_solver_graph(p, coupling, Nmax, f="coupling_light_graph.png")
   # save_solver_log_graph(p, coupling, Nmax, f="coupling_log_light_graph.png")
   # save_solver_graph(p, greedy, Nmax, f="greedy_light_graph.png")
   # save_solver_log_graph(p, greedy, Nmax, f="greedy_log_dense_graph.png")