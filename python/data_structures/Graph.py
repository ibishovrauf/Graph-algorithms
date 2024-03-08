from .Node import Node

class Graph:
    def __init__(self, directed: bool = True, weighted: bool = False):
        self.directed = directed
        self.weighted = weighted
        self.nodes = {}

    def add_node(self, value: str):
        self.nodes[value] = Node(value)

    def add_edge(self, value1, value2, weight=None):
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        node1.add_neighbor(node2, self.directed, self.weighted, weight)

    def get_nodes(self):
        return list(self.nodes.keys())

    def get_edges(self):
        edges = []
        for node in self.nodes.values():
            edges.extend(node.get_outgoing_edges())
        return edges
    
    def get_neighbors(self, value):
        node = self.nodes[value]
        neighbors = node.get_outgoing_nodes()
        if self.directed:
            neighbors.extend(node.get_incoming_nodes())
        return neighbors

    def get_edge_weight(self, value1, value2):
        if not self.weighted:
            return "The Graph is not weighted"
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        return node1.get_weight(node2)

    def is_directed(self):
        return self.directed

    def is_weighted(self):
        return self.weighted
