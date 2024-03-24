from data_structures import Graph
def depth_first_search(graph: Graph, start_value):
    """
    Performs a depth-first search in the graph from a start node using recursion.

    Args:
        graph (Graph): The graph to perform the search on.
        node_value (any): The value of the node from which the search starts.

    Returns:
        list: A list of node values representing the order in which the nodes were visited.
    """
    dfs_order = []

    def dfs(node):
        node.visit()
        dfs_order.append(node.get_value())

        for neighbor in node.get_outgoing_nodes():
            if not neighbor.is_visited():
                dfs(neighbor)

    dfs(graph.get_node(start_value))
    return dfs_order
