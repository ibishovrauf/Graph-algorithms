from data_structures import Graph2D
from visulization import save_graph

def main():
    graph = Graph2D()

    # Add nodes to the graph
    graph.add_node("A", x=-1, y=1)
    graph.add_node("B", x=0, y=0)
    graph.add_node("C", x=0, y=1)
    graph.add_node("D", x=0, y=-1)
    graph.add_node("F", x=1, y=-1)
    graph.add_node("E", x=-1, y=0)

    print("Nodes:", graph.get_nodes())
    print("Edges:", graph.get_edges())
    save_graph(graph, "test.pkl")

if __name__ == "__main__":
    main()
