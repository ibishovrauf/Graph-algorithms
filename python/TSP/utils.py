from typing import List
from data_structures import Edge

def has_cycle(edges):
    # Step 1: Create an adjacency list from the edge list
    graph = {}
    for u, v in list(map(lambda x: (x.get_node1().get_value(), x.get_node2().get_value()), edges)):
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    # Helper function for DFS
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False
    
    visited = set()
    # Step 3: Check each unvisited node for a cycle
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False


def generate_tsp_tour(eulerian_tour):
    # Initialize an empty set to keep track of visited vertices.
    visited = set()
    
    # Initialize an empty list to store the TSP tour.
    tsp_tour = []
    
    for vertex in eulerian_tour:
        # If the vertex has not been visited, add it to the TSP tour.
        if vertex not in visited:
            visited.add(vertex)
            tsp_tour.append(vertex)
    
    # Optionally, you can add the starting vertex at the end to complete the tour.
    # tsp_tour.append(tsp_tour[0])
    
    return tsp_tour + [tsp_tour[0]]
