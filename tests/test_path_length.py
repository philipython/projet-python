import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph
from solver import Solver
class TestBestPath(unittest.TestCase):
    def test_find_best_path(self):
        grid = Grid(2, 3 , [[1, 4, 6], [2, 3, 5]])
        grid.path_graph = Graph(grid.grids_graph())
        grid.path_graph.edges = grid.all_edges()

        best_path = grid.find_best_path()
        print(best_path)
        print("bfs length:", len(best_path)-1)
        naive_solver = Solver(grid)
        naive_solver_solution = naive_solver.get_solution()
        print("naive solver moves:", len(naive_solver_solution))

if __name__ == '__main__':
    unittest.main()