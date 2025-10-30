import matplotlib.pyplot as plt
from basic_operations import *
from time import time
import numpy as np
from math import *
import networkx as nx

def test_vc_solver(p, vc_solver, max_size):
   x_points = []
   y_points = []
   for n in range(1, max_size+1):
      g = generate_random_graph(n, p)
      start = time()
      vc_solver(g)
      duration = time() - start
      x_points.append(n)
      y_points.append(duration)
   return np.array(x_points), np.array(y_points)

def show_graph(x_points, y_points, x_label="Size of the graph (number of vertices)", y_label=""):
   plt.plot(x_points, y_points, marker='o')
   plt.xlabel(x_label)
   plt.ylabel(y_label)
   plt.show()

def show_solver_graph(p, vc_solver, max_size):
   x_points, y_points = test_vc_solver(p, vc_solver, max_size)
   show_graph(x_points, y_points, y_label="Time in seconds")

def show_solver_log_graph(p, vc_solver, max_size):
   x_points, y_points = test_vc_solver(p, vc_solver, max_size)
   show_graph(x_points, [log(t) for t in y_points], y_label="log of time in seconds")

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
      line_nbr_for_start_of_node_list+number_of_nodes
        ])
   list_of_edges = data[
      line_nbr_for_start_of_edge_list :
      line_nbr_for_start_of_edge_list + number_of_edges
      ]
   for edge in list_of_edges :
      g.add_edge(*edge.split(" "))
   print(g.nodes)
   print(g.edges)
   return 0

if __name__ == "__main__":
   parse_graph("test.txt")
