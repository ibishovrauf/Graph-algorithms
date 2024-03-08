from .Edge import Edge

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.outgoing_edges = {}
        self.incoming_edges = {}
    
    def add_neighbor(self, node: 'Node', directed: bool = True, weighted: bool = False, weight: int = None) -> None:
        edge = Edge(self, node, directed, weighted, weight)
        self.outgoing_edges[node] = edge
        node.incoming_edges[self] = edge
        if not directed:
            self.incoming_edges[node] = edge
            node.outgoing_edges[self] = edge
    
    def get_weight(self, node):
        edge = self.outgoing_edges.get(node, None)
        if not edge:
            return "there is not edge between this nodes"
        return edge.get_weight()

    def get_incoming_nodes(self) -> list:
        return list(self.incoming_edges.keys())
    
    def get_incoming_edges(self) -> list:
        return list(self.incoming_edges.values())
    
    def get_outgoing_nodes(self) -> list:
        return list(self.outgoing_edges.keys())
    
    def get_outgoing_edges(self) -> list:
        return list(self.outgoing_edges.values())
    
    def __str__(self) -> str:
        return "Node " + self.value