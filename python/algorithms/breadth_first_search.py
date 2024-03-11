from collections import deque
from data_structures import Graph

def breadth_first_search(graph: Graph, start_value):
    """
    Performs a breadth-first search in the graph from a start node.

    Parameters
    ----------
    graph : Graph
        The graph to perform the search on.
    start_value : any
        The value of the node from which the search starts.

    Returns
    -------
    list
        A list of node values representing the order in which the nodes were visited.
    """
    start_node = graph.nodes[start_value]
    visited = {start_value}
    queue = deque([start_node])
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node.value)

        for neighbor in node.get_outgoing_nodes():
            if neighbor.value not in visited:
                visited.add(neighbor.value)
                queue.append(neighbor)

    return bfs_order
