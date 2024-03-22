from data_structures import Graph
from visulization import save_graph

def main():
    graph = Graph(weighted=True)

    # Add nodes to the graph
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("F")
    graph.add_node("E")

    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('C', 'D', weight=12)
    graph.add_edge('D', 'B', weight=12)
    graph.add_edge('C', 'B', weight=12)
    graph.add_edge('A', 'D', weight=12)
    graph.add_edge('A', 'C', weight=12)

    print("Nodes:", graph.get_nodes())
    print("Edges:", graph.get_edges())
    graph.construct_adjacency_matrix()
    print(graph.get_adjacency_matrix())

if __name__ == "__main__":
    main()
