from data_structures import Node

class Egde:
    def __init__(self, node_1: Node, node_2: Node, directed: bool = True, weighted: bool = False, weight: int = None) -> None:
        self.node_1 = node_1
        self.node_2 = node_2
        self.directed = directed
        self.weighted = weighted
        if self.weighted:
            self.weight = weighted
        
    def is_directed(self):
        return self.directed
    
    def is_weighted(self):
        return self.weighted
    
    def get_weight(self):
        if self.is_weighted:
            return self.weight
        return "The Edge is not weighted"
