from data_structures import *

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node1.add_neighbor(node2)
    print(node1.outgoing_edges)
    print(node1.incoming_edges)