class Edge:
    def __init__(self, node_1: 'Node', node_2: 'Node', directed: bool = True, weighted: bool = False, weight: int = None) -> None:
        """
        Initialize an Edge object.

        Args:
            node_1 (Node): The first node connected by the edge.
            node_2 (Node): The second node connected by the edge.
            directed (bool, optional): Whether the edge is directed. Defaults to True.
            weighted (bool, optional): Whether the edge is weighted. Defaults to False.
            weight (int, optional): The weight of the edge if it is weighted. Defaults to None.
        """
        self.node_1 = node_1
        self.node_2 = node_2
        self.directed = directed
        self.weighted = weighted
        if self.weighted:
            self.weight = weight
        
    def is_directed(self) -> bool:
        """
        Check if the edge is directed.

        Returns:
            bool: True if the edge is directed, False otherwise.
        """
        return self.directed
    
    def is_weighted(self) -> bool:
        """
        Check if the edge is weighted.

        Returns:
            bool: True if the edge is weighted, False otherwise.
        """
        return self.weighted
    
    def get_weight(self):
        """
        Get the weight of the edge if it is weighted.

        Returns:
            int or str: The weight of the edge if it is weighted, or a string indicating that the edge is not weighted.
        """
        if self.is_weighted:
            return self.weight
        return "The Edge is not weighted"

    def get_node1(self):
        """
        Retrieves the starting node of the directed edge.

        Returns:
            Node: The starting node of the edge.
        """
        return self.node_1

    def get_node2(self):
        """
        Retrieves the ending node of the directed edge.

        Returns:
            int or str: The ending node of the edge.
        """
        return self.node_2

    def __str__(self) -> str:
        """
        Get a string representation of the edge.

        Returns:
            str: A string representation of the edge, showing its connection between nodes.
        """
        if self.directed:
            return str(self.node_1) + "->" + str(self.node_2)
        return str(self.node_1) + "<->" + str(self.node_2)
    
    def __contains__(self, item):

        return item in [self.node_1.get_value(), self.node_2.get_value()]

    def __sub__(self, item):
        data = {self.node_1.get_value(), self.node_2.get_value()}
        data.remove(item)
        return data.pop()
    
    def __eq__(self, edge: object) -> bool:
        return sorted(self.node_1.get_value() + self.node_2.get_value()) == sorted(edge.get_node1().get_value() + edge.get_node2().get_value())