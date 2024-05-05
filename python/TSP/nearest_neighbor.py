from data_structures import Graph2D, Node, Edge
import matplotlib.pyplot as plt
import networkx as nx
import math
from itertools import permutations
import pickle

def nearest_neighbor(graph: Graph2D):
    n = len(graph.get_nodes())
    route = []
    curr_node: Node = graph.get_node("A")
    total_dist = 0
    for _ in range(n):
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            if node_key == curr_node.get_value():
                color = "#007bff"
            elif node_value.is_visited():
                color = "#737272"
            else:
                color = "#E0E0E0"
            G.add_node(node_key, pos=(node_value.x, node_value.y), color=color)
        for edge in route:
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='b', weight=edge.get_weight())
        
        curr_node.visit()
        min_dist = float("inf")
        min_edge = None
        next_ = None
        for neighbour in curr_node.get_outgoing_nodes():
            if not neighbour.is_visited():
                edge: Edge = curr_node.get_edge(neighbour)
                G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='r', weight=edge.get_weight())
                if edge.get_weight() < min_dist:
                    min_edge = edge
                    min_dist = edge.get_weight()
                    next_ = neighbour
        if next_:
            curr_node = next_
            route.append(min_edge)
            total_dist += min_dist
        else:
            last_edge: Edge = graph.get_edge(curr_node.get_value(), "A")
            total_dist += last_edge.get_weight()
            route.append(last_edge)
        pos = nx.get_node_attributes(G, 'pos')
        node_color = nx.get_node_attributes(G, 'color').values()
        colors = nx.get_edge_attributes(G,'color').values()
        nx.draw(G, pos, with_labels=True, node_size=200, node_color=node_color, edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)
        plt.pause(1)
    plt.clf()
    img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
    plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
    G = nx.Graph()
    for node_key, node_value in graph.nodes.items():
        G.add_node(node_key, pos=(node_value.x, node_value.y), color="#737272")
    for edge in route:
        G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='b', weight=edge.get_weight())
    pos = nx.get_node_attributes(G, 'pos')
    node_color = nx.get_node_attributes(G, 'color').values()
    colors = nx.get_edge_attributes(G,'color').values()
    nx.draw(G, pos, with_labels=True, node_size=200, node_color=node_color, edge_color=colors)
    if graph.is_weighted():
        labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show(block=False)
    plt.pause(3)

    return total_dist
def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph

if __name__ == "__main__":
    pickle_file = './data/6cities.pkl'
    graph = read_graph_from_pickle(pickle_file, 0)
    print(nearest_neighbor(graph))