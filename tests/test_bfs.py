
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_bfs(unittest.TestCase):
    def test_graph1(self):
        graph = Graph("./input/graph1.in")
        graph.bfs()
if __name__ == '__main__':
    unittest.main()