from data_structures import Graph, PriorityQueue
import math

def dijkstra(graph: Graph, start_node):
    if not graph.is_weighted():
        return 'The Graph is not weihted'
    if not graph.is_directed():
        return 'The Graph is not directed'
    distances = {}
    for node in graph.get_nodes():
        distances[node] = math.inf

    queue = PriorityQueue()
    distances[start_node] = 0
    start_node = graph.get_node(start_node)
    for edge in start_node.get_outgoing_edges():
        queue.push(edge, edge.get_weight())
        distances[edge.get_node2().value] = edge.get_weight()
    while queue:
        print(queue)
        distance, _, edge = queue.pop()
        node = edge.get_node2()
        for outgoing_edge in node.get_outgoing_edges():
            distances[outgoing_edge.get_node2().value] = min(distances[outgoing_edge.get_node2().value], distance + outgoing_edge.get_weight())
            queue.push(outgoing_edge, distances[outgoing_edge.get_node2().value])
    return distances