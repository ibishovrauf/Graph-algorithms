from data_structures import Graph, PriorityQueue
from .utils import find_shortest_path
import math


def dijkstra(graph: Graph, start_node, search_node, cost: bool = False):
    """
    Dijkstra's algorithm to find the shortest path between two nodes in a weighted directed graph.

    Args:
        graph (Graph): The graph in which to perform the search.
        start_node: The starting node for the path search.
        search_node: The target node to find the shortest path to.
        cost (bool, optional): If True, returns both the shortest path and its cost. 
                               Defaults to False.

    Returns:
        If `cost` is False:
            list: The shortest path from `start_node` to `search_node`, represented as a list of node values.
        If `cost` is True:
            tuple: A tuple containing two elements:
                list: The shortest path from `start_node` to `search_node`, represented as a list of node values.
                float: The cost of the shortest path from `start_node` to `search_node`.
        
    Note:
        - If the graph is not weighted or not directed, the function returns appropriate error messages.
        - If there is no path from `start_node` to `search_node`, returns an empty list.
    """
    if not graph.is_weighted():
        return 'The Graph is not weihted'
    if not graph.is_directed():
        return 'The Graph is not directed'
    distances = {}
    previous_visited = {}
    for node in graph.get_nodes():
        distances[node] = math.inf
        previous_visited[node] = None

    queue = PriorityQueue()
    distances[start_node] = 0
    start_node = graph.get_node(start_node)
    for edge in start_node.get_outgoing_edges():
        queue.push(edge, edge.get_weight())
        distances[edge.get_node2().get_value()] = edge.get_weight()
        previous_visited[edge.get_node2().get_value()] = edge.get_node1().get_value()

    while queue:
        distance, _, edge = queue.pop()
        node = edge.get_node2()
        if node.is_visited():
            continue
        node.visit()
        if distances[edge.get_node2().get_value()] < distance:
            continue 
        for outgoing_edge in node.get_outgoing_edges():
            distances[outgoing_edge.get_node2().get_value()] = min(distances[outgoing_edge.get_node2().get_value()], distance + outgoing_edge.get_weight())
            previous_visited[outgoing_edge.get_node2().get_value()] = outgoing_edge.get_node1().get_value()
            queue.push(outgoing_edge, distances[outgoing_edge.get_node2().get_value()])
        if previous_visited[search_node]: break
    if cost:
        return find_shortest_path(previous_visited, start_node, search_node), distances[search_node]
    return find_shortest_path(previous_visited, start_node, search_node)
