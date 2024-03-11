import unittest
from data_structures import Graph
from algorithms import breadth_first_search

class TestBreadthFirstSearch(unittest.TestCase):
    def test_bfs(self):
        graph = Graph()
        graph.add_nodes(['A', 'B', 'C', 'D', 'E'])
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'E')

        bfs_result = breadth_first_search(graph, 'A')

        self.assertEqual(bfs_result, ['A', 'B', 'C', 'D', 'E'])

if __name__ == '__main__':
    unittest.main()
