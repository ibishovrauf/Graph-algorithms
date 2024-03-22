import numpy as np

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


def construct_shortest_path(dp: np.ndarray, next: np.ndarray, start: int, end: int) -> list:
    """
    Constructs the shortest path between two nodes using dynamic programming results.

    Parameters:
    - dp (numpy.ndarray): A 3D array representing the dynamic programming table.
    - next (numpy.ndarray): A 2D array representing the next node in the shortest path.
    - start (int): The index of the starting node.
    - end (int): The index of the ending node.

    Returns:
    - list or None: A list of node indices representing the shortest path from start to end.
                    Returns None if no path exists.

    Note:
    - This function works on the assumption that the graph is represented using dynamic programming
      results (dp) and the next node pointers (next).
    """
    path = []
    print(next)
    if dp[-1, start, end] == np.inf:
        return path
    
    at = start
    while at != end:
        if at == -1:
            return None
        path.append(int(at))
        at = next[int(at), int(end)]
    if next[int(at), int(end)] == -1:
        return None
    path.append(end)
    return path