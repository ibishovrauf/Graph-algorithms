def find_shortest_path(path_dict: dict, start_node, last_node):
    """
    Finds the shortest path between two nodes using a dictionary representing the previous node in the path.

    Args:
        path_dict (dict): A dictionary where keys are nodes and values are the previous nodes in the shortest path.
        start_node: The starting node of the path.
        last_node: The target node of the path.

    Returns:
        str: A string representing the shortest path from `start_node` to `last_node`.
             Nodes are separated by '->'. If no path exists, returns an appropriate error message.
    """
    if not path_dict[last_node]:
        return f"No path found between nodes {start_node} and {last_node}"
    path = []
    while last_node:
        path.insert(0, last_node)
        last_node = path_dict[last_node]
    return "->".join(path)
