from .Node import Node

class Graph:
    def __init__(self, directed: bool = True, weighted: bool = False):
        """
        Initialize a Graph object.

        Args:
            directed (bool, optional): Whether the graph is directed. Defaults to True.
            weighted (bool, optional): Whether the graph is weighted. Defaults to False.
        """
        self.directed = directed
        self.weighted = weighted
        self.nodes = {}

    def add_node(self, value: str):
        """
        Add a node to the graph.

        Args:
            value (str): The value of the node to be added.
        """
        self.nodes[value] = Node(value)

    def add_edge(self, value1, value2, weight=None):
        """
        Add an edge to the graph.

        Args:
            value1: The value of the first node connected by the edge.
            value2: The value of the second node connected by the edge.
            weight (optional): The weight of the edge. Defaults to None.
        """
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        node1.add_neighbor(node2, self.directed, self.weighted, weight)

    def get_nodes(self):
        """
        Get the nodes in the graph.

        Returns:
            list: A list of values of all nodes in the graph.
        """
        return list(self.nodes.keys())

    def get_edges(self):
        """
        Get the edges in the graph.

        Returns:
            list: A list of all edges in the graph.
        """
        edges = []
        for node in self.nodes.values():
            edges.extend(node.get_outgoing_edges())
        return edges
    
    def get_neighbors(self, value):
        """
        Get the neighbors of a node in the graph.

        Args:
            value: The value of the node whose neighbors are to be retrieved.

        Returns:
            list: A list of values of neighboring nodes.
        """
        node = self.nodes[value]
        neighbors = node.get_outgoing_nodes()
        if self.directed:
            neighbors.extend(node.get_incoming_nodes())
        return neighbors

    def get_edge_weight(self, value1, value2):
        """
        Get the weight of an edge in the graph.

        Args:
            value1: The value of the first node connected by the edge.
            value2: The value of the second node connected by the edge.

        Returns:
            int or str: The weight of the edge, or a string indicating that the graph is not weighted.
        """
        if not self.weighted:
            return "The Graph is not weighted"
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        return node1.get_weight(node2)

    def is_directed(self):
        """
        Check if the graph is directed.

        Returns:
            bool: True if the graph is directed, False otherwise.
        """
        return self.directed

    def is_weighted(self):
        """
        Check if the graph is weighted.

        Returns:
            bool: True if the graph is weighted, False otherwise.
        """
        return self.weighted
