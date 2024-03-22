from algorithms import floyd_warshall
from data_structures import Graph

def main():
    graph = Graph(weighted=True)

    # Add nodes to the graph
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=5)
    graph.add_edge('C', 'D', weight=1)
    graph.add_edge('D', 'B', weight=2)

    print("Nodes:", graph.get_nodes())
    print("Edges:", graph.get_edges())
    graph.construct_adjacency_matrix()
    print(floyd_warshall(graph, 'A', 'B'))

if __name__ == "__main__":
    main()
