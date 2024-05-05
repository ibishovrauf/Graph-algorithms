from data_structures import Graph2D
from visulization import save_graph

def main():
    graph = Graph2D()
    
    graph.add_node('A', 8, 0)
    graph.add_node('B', 7, -3)
    graph.add_node('C', 5, -5)
    graph.add_node('E', 0, -7)
    graph.add_node('F', 3, 6)
    graph.add_node('H', -7, -3)
    graph.add_node('W', -8, 0)
    graph.add_node('R', -7, 3)
    graph.add_node('T', -5, 5)
    save_graph(graph, "test1.pkl")

if __name__ == "__main__":
    main()
