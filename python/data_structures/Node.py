from math import sqrt
from .Edge import Edge

class Node:
    def __init__(self, value) -> None:
        """
        Initialize a Node object.

        Args:
            value: The value of the node.
        """
        self.value = value
        self.outgoing_edges = {}
        self.incoming_edges = {}
    
    def add_neighbor(self, node: 'Node', directed: bool = True, weighted: bool = False, weight: int = None) -> None:
        """
        Add a neighbor node to the current node.

        Args:
            node (Node): The node to be connected as a neighbor.
            directed (bool, optional): Whether the edge is directed. Defaults to True.
            weighted (bool, optional): Whether the edge is weighted. Defaults to False.
            weight (int, optional): The weight of the edge. Defaults to None.
        """
        edge = Edge(self, node, directed, weighted, weight)
        self.outgoing_edges[node] = edge
        node.incoming_edges[self] = edge
        if not directed:
            self.incoming_edges[node] = edge
            node.outgoing_edges[self] = edge
    
    def get_weight(self, node):
        """
        Get the weight of the edge between the current node and a neighbor node.

        Args:
            node (Node): The neighbor node.

        Returns:
            int or str: The weight of the edge, or a message indicating no edge exists between the nodes.
        """
        edge = self.outgoing_edges.get(node, None)
        if not edge:
            return "there is not edge between this nodes"
        return edge.get_weight()

    def get_incoming_nodes(self) -> list:
        """
        Get the incoming neighbor nodes of the current node.

        Returns:
            list: A list of incoming neighbor nodes.
        """
        return list(self.incoming_edges.keys())
    
    def get_incoming_edges(self) -> list:
        """
        Get the incoming edges of the current node.

        Returns:
            list: A list of incoming edges.
        """
        return list(self.incoming_edges.values())
    
    def get_outgoing_nodes(self) -> list:
        """
        Get the outgoing neighbor nodes of the current node.

        Returns:
            list: A list of outgoing neighbor nodes.
        """
        return list(self.outgoing_edges.keys())
    
    def get_outgoing_edges(self) -> list:
        """
        Get the outgoing edges of the current node.

        Returns:
            list: A list of outgoing edges.
        """
        return list(self.outgoing_edges.values())
    
    def __str__(self) -> str:
        """
        Get a string representation of the node.

        Returns:
            str: A string representation of the node.
        """
        return "Node " + self.value



from math import sqrt

class Node2D(Node):
    """A node in a 2D graph."""

    def __init__(self, value, x, y) -> None:
        """
        Initialize a 2D node.

        Initializes the node with a value and its coordinates.

        Parameters:
            value: The value of the node.
            x: The x-coordinate of the node.
            y: The y-coordinate of the node.

        Returns:
            None
        """
        super().__init__(value)
        self.x = x
        self.y = y

    def add_neighbor(self, node: Node) -> None:
        """
        Add a neighbor to the node.

        Creates an edge between this node and the given node, and adds it to both nodes.

        Parameters:
            node (Node): The node to connect as a neighbor.

        Returns:
            None
        """
        edge = Edge(self, node, weight=self.distance(node))
        self.outgoing_edges[node] = edge
        node.incoming_edges[self] = edge
        self.incoming_edges[node] = edge
        node.outgoing_edges[self] = edge

    def distance(self, node) -> float:
        """
        Calculate the Euclidean distance between this node and another node.

        Parameters:
            node (Node): The other node to calculate distance to.

        Returns:
            float: The Euclidean distance between this node and the given node.
        """
        return sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)
