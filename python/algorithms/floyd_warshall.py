from data_structures import Graph
from .utils import construct_shortest_path
import numpy as np

def floyd_warshall(graph: Graph, start_node, search_node):
    """
    Applies the Floyd-Warshall algorithm to find the shortest path between two nodes in a graph.

    Parameters:
        graph (Graph): An instance of the Graph class representing the graph.
        start_node: The node from which to start the path search.
        search_node: The node to which the shortest path is to be found.

    Returns:
        str: A string representing the shortest path between the start_node and search_node,
             formatted as "node1->node2->...->search_node".

    Note:
        This function assumes that the graph is weighted.

    Raises:
        ValueError: If either start_node or search_node is not present in the graph.
    """

    graph.construct_adjacency_matrix()
    adj = graph.get_adjacency_matrix()
    n = adj.shape[0]
    without_edges = np.where(adj == 0)
    adj[without_edges] = np.inf
    next = np.arange(n)
    next = next[np.newaxis, :] + np.zeros((n, n), dtype=float)
    next[without_edges] = np.nan

    np.fill_diagonal(adj, 0)
    dp = np.tile(adj, (n, 1, 1))
    
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if dp[k-1, i, j] > dp[k-1, i, k] + dp[k-1, k, j]:
                    dp[k, i, j] = dp[k-1, i, k] + dp[k-1, k, j]
                    next[i, j] = next[i, k]
    path_int = construct_shortest_path(dp, next, graph.get_index_of_node(start_node), graph.get_index_of_node(search_node))
    path = "->".join(map(lambda x: graph.get_node_val_from_index(x), path_int))
    return path