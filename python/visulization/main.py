import pickle
import matplotlib.pyplot as plt
import networkx as nx
from TSP import brute_force_TSP

def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph
    

def visualize_graph_as_map():
    f = True
    while True:
        pickle_file = './data/test.pkl'
        graph = read_graph_from_pickle(pickle_file, 0)
        brute_force_TSP(graph)
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()

        for node_key, node_value in graph.nodes.items():
            G.add_node(node_key, pos=(node_value.x, node_value.y))
        
        for edge in graph.get_edges():
            if graph.is_weighted():
                G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='r', weight=edge.get_weight())
            else:
                G.add_edge(edge.get_node1(), edge.get_node2())
        
        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_edge_attributes(G,'color').values()
        nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)        

        plt.pause(5)

visualize_graph_as_map()
