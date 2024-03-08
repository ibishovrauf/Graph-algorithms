
class Edge:
    def __init__(self, node_1: 'Node', node_2: 'Node', directed: bool = True, weighted: bool = False, weight: int = None) -> None:
        self.node_1 = node_1
        self.node_2 = node_2
        self.directed = directed
        self.weighted = weighted
        if self.weighted:
            self.weight = weight
        
    def is_directed(self):
        return self.directed
    
    def is_weighted(self):
        return self.weighted
    
    def get_weight(self):
        if self.is_weighted:
            return self.weight
        return "The Edge is not weighted"

    def __str__(self) -> str:
        if self.directed:
            return str(self.node_1) + "->" + str(self.node_2)
        return str(self.node_1) + "<->" + str(self.node_2)