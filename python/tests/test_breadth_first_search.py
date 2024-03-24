import unittest
from data_structures import Graph
from algorithms import breadth_first_search

class TestBreadthFirstSearch(unittest.TestCase):
    """
    Test case for the breadth-first search algorithm.
    """
    def test_bfs(self):
        """
        Test the breadth-first search algorithm on a graph.
        The graph has nodes 'A', 'B', 'C', 'D', 'E' with edges as follows:
        'A' -> 'B', 'A' -> 'C', 'B' -> 'D', 'C' -> 'E'.
        The breadth-first search starts from node 'A'.
        The expected result is ['A', 'B', 'C', 'D', 'E'].
        """
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
