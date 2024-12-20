from algorithms import dijkstra
from data_structures import Graph

if __name__ == "__main__":
    def create_simple_graph():
        graph = Graph(weighted=True)

        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')
        graph.add_node('E')

        graph.add_edge('A', 'B', 4)
        graph.add_edge('A', 'C', 1)
        graph.add_edge('C', 'E', 3)
        graph.add_edge('B', 'D', 1)
        graph.add_edge('C', 'B', 2)
        graph.add_edge('C', 'D', 5)
        graph.add_edge('D', 'E', 3)
        return graph
    

    print(dijkstra(create_simple_graph(), 'A', 'E', True))
