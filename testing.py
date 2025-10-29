import matplotlib.pyplot as plt
from basic_operations import *
from time import time
import numpy as np
from math import *

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
