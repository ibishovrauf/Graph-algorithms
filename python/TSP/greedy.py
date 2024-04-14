from data_structures import Graph2D, Edge
import matplotlib.pyplot as plt
import networkx as nx
from .utils import has_cycle
import pickle
from collections import defaultdict

def greedy(graph: Graph2D):
    def zero():
        return 0
    n = len(graph.get_nodes())
    node_count = defaultdict(zero)
    route = []
    total_dist = 0
    for _ in range(n):
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            color = "#E0E0E0"
            G.add_node(node_key, pos=(node_value.x, node_value.y), color=color)
        for edge in route:
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='b', weight=edge.get_weight())

        min_dist = float("inf")
        min_edge = None
        for edge in graph.get_edges():
            if has_cycle(route+[edge]):
                if _+1 != n:
                    continue
            if node_count[edge.get_node1().get_value()] == 2:
                continue
            if node_count[edge.get_node2().get_value()] == 2:
                continue
            if edge in route:
                continue
            if edge.get_weight() < min_dist:
                min_dist = edge.get_weight()
                min_edge = edge
        G.add_edge(min_edge.get_node1().get_value(), min_edge.get_node2().get_value(), color='b', weight=min_edge.get_weight())
        pos = nx.get_node_attributes(G, 'pos')
        node_color = nx.get_node_attributes(G, 'color').values()
        colors = nx.get_edge_attributes(G,'color').values()
        nx.draw(G, pos, with_labels=True, node_size=200, node_color=node_color, edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)
        plt.pause(1)
        route.append(min_edge)
        total_dist += min_dist
        node_count[min_edge.get_node1().get_value()] += 1
        node_count[min_edge.get_node2().get_value()] += 1
    return total_dist
    
def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph

if __name__ == "__main__":
    pickle_file = './data/test.pkl'
    graph = read_graph_from_pickle(pickle_file, 0)
    print(greedy(graph))