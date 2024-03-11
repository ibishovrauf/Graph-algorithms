from data_structures import Graph
def depth_first_search(graph: Graph, node_value):
    """
    Performs a depth-first search in the graph from a start node using recursion.

    Parameters
    ----------
    graph : Graph
        The graph to perform the search on.
    node_value : any
        The value of the node from which the search starts.

    Returns
    -------
    list
        A list of node values representing the order in which the nodes were visited.
    """
    visited = set()
    dfs_order = []

    def dfs(node_value):
        visited.add(node_value)
        dfs_order.append(node_value)

        for neighbor in graph.nodes[node_value].get_outgoing_nodes():
            if neighbor.value not in visited:
                dfs(neighbor.value)

    dfs(node_value)
    return dfs_order
