from data_structures import Graph2D
import matplotlib.pyplot as plt
import networkx as nx
import math
from itertools import permutations
import pickle

def brute_force_TSP(graph: Graph2D):
    nodes = graph.get_nodes()
    perm = permutations(nodes[1:])

    perm_list = list(perm)
    min_dist = math.inf
    for permutation in perm_list:
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            G.add_node(node_key, pos=(node_value.x, node_value.y))

        prev = nodes[0]
        dist = 0
        for node in list(permutation)+[nodes[0]]:
            edge = graph.get_edge(prev, node)
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='r', weight=edge.get_weight())
            dist += edge.get_weight()
            prev = node
        min_dist = min(min_dist, dist)
        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_edge_attributes(G,'color').values()
        plt.text(0.5, 1.1, f'min Dist: {min_dist} \n curr dist: {dist}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

        nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)        

        plt.pause(0.3)
    return min_dist

def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph

if __name__ == "__main__":
    pickle_file = './data/test.pkl'
    graph = read_graph_from_pickle(pickle_file, 0)
    print(brute_force_TSP(graph))