from data_structures import Graph

def main():
    # Create a weighted graph
    graph = Graph(directed=True, weighted=True)

    # Add nodes to the graph
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    # Add weighted edges to the graph
    graph.add_edge("A", "B", weight=5)
    graph.add_edge("B", "C", weight=7)
    graph.add_edge("C", "D", weight=3)
    graph.add_edge("D", "A", weight=2)

    # Test various functions
    print("Nodes:", graph.get_nodes())
    print("Edges:", graph.get_edges())
    print("Neighbors of A:")
    for i in graph.get_neighbors("A"):
        print(str(i))
    print("Edge weight between A and B:", graph.get_edge_weight("A", "B"))
    print("Is graph directed?", graph.is_directed())
    print("Is graph weighted?", graph.is_weighted())

if __name__ == "__main__":
    main()
