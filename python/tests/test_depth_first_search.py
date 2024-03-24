import unittest
from data_structures import Graph
from algorithms import depth_first_search

class TestDepthFirstSearch(unittest.TestCase):
    """
    Test case for the depth-first search algorithm.
    """
    def test_dfs_recursive(self):
        """
        Test the depth-first search algorithm on a graph.
        The graph has nodes 'A', 'B', 'C', 'D', 'E' with edges as follows:
        'A' -> 'B', 'A' -> 'C', 'B' -> 'D', 'C' -> 'E'.
        The depth-first search starts from node 'A'.
        The expected result is ['A', 'B', 'D', 'C', 'E'].
        """
        graph = Graph()
        graph.add_nodes(['A', 'B', 'C', 'D', 'E'])
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'E')

        dfs_result = depth_first_search(graph, 'A')

        self.assertEqual(dfs_result, ['A', 'B', 'D', 'C', 'E'])

if __name__ == '__main__':
    unittest.main()
