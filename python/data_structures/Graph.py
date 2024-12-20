from .Node import Node, Node2D

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

    def add_node(self, value):
        """
        Add a node to the graph.

        Args:
            value (str): The value of the node to be added.
        """
        self.nodes[value] = Node(value)

    def add_nodes(self, values):
        """
        Add list of values to the graph

        Args:
            values (list): A list of values to be added as nodes to the graph.
        """
        for value in values:
            self.add_node(value)
            
            
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

    def get_node(self, value):
        """
        Retrieves a node from the graph based on its value.

        Args:
            value: The value identifying the node to retrieve.

        Returns:
            Node or str: The node corresponding to the given value if found in the graph.
                        If the node with the given value is not found, returns an appropriate error message.
        """
        if value in self.nodes:
            return self.nodes[value]
        return f"The Node {value} is not in the graph"

class Graph2D(Graph):
    """A 2D graph representation inheriting from Graph class."""

    def __init__(self):
        """
        Initialize a 2D graph.

        Initializes the 2D graph with width and height parameters set to True.

        Parameters:
            None

        Returns:
            None
        """
        super().__init__(True, True)
    
    def add_node(self, value: str, x: int, y: int):
        """
        Add a new node to the graph with its coordinates.

        This method creates a new node with the given value and coordinates, and then connects it
        to all existing nodes in the graph.

        Parameters:
            value (str): The value of the new node.
            x (int): The x-coordinate of the new node.
            y (int): The y-coordinate of the new node.

        Returns:
            None
        """
        new_node = Node2D(value, x, y)
        for node in list(self.nodes.values()):
            self.add_edge(node, new_node)
        self.nodes[value] = new_node
        
    def add_edge(self, node1: 'Node', node2: 'Node'):
        """
        Add an edge between two nodes in the graph.

        This method adds an edge between the given nodes by making one node a neighbor of the other.

        Parameters:
            node1 (Node): The first node.
            node2 (Node): The second node.

        Returns:
            None
        """
        node1.add_neighbor(node2)
