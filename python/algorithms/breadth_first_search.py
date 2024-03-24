from collections import deque
from data_structures import Graph

def breadth_first_search(graph: Graph, start_value):
    """
    Performs a breadth-first search in the graph from a start node.

    Args:
        graph (Graph): The graph to perform the search on.
        start_value (any): The value of the node from which the search starts.

    Returns:
        list: A list of node values representing the order in which the nodes were visited.
    """
    start_node = graph.get_node(start_value)
    start_node.visit()
    queue = deque([start_node])
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node.get_value())

        for neighbor in node.get_outgoing_nodes():
            if not neighbor.is_visited():
                neighbor.visit()
                queue.append(neighbor)

    return bfs_order
