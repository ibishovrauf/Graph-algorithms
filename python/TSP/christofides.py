from data_structures import Graph2D
from .utils import generate_tsp_tour
import pickle
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def christofides(graph: Graph2D):
    if len(graph.nodes) == 0:
        return []

    mst = []
    start_node = next(iter(graph.nodes.values()))  # Starting from an arbitrary node
    explored = set([start_node.value])
    edges = [(edge.get_weight(), edge.get_node1().get_value(), edge.get_node2().get_value()) for edge in start_node.get_outgoing_edges()]

    heapq.heapify(edges)
    
    node_connection = {}
    while edges:
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            G.add_node(node_key, pos=(node_value.x, node_value.y))

        weight, from_node, to_node = heapq.heappop(edges)

        if to_node not in explored:
            explored.add(to_node)
            mst.append(graph.get_edge(from_node, to_node))
            node_connection[from_node] = node_connection.get(from_node, 0) + 1
            node_connection[to_node] = node_connection.get(to_node, 0) + 1

            for edge in graph.nodes[to_node].get_outgoing_edges():
                if edge.get_node2().get_value() not in explored:
                    heapq.heappush(edges, (edge.get_weight(), to_node, edge.get_node2().get_value()))
        for edge in mst:
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='r', weight=edge.get_weight())
        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_edge_attributes(G,'color').values()

        nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)

        plt.pause(0.3)
    odd_nodes = []
    for key, val in node_connection.items():
        if val % 2 == 1:
            odd_nodes.append(key)
    edges = []
    for from_node in odd_nodes:
        for to_node in odd_nodes:
            if from_node != to_node:
                edges.append((graph.get_edge_weight(from_node, to_node), from_node, to_node))

    explored = set()
    mst_1 = []
    while len(mst_1) != len(odd_nodes)//2:
        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            G.add_node(node_key, pos=(node_value.x, node_value.y))

        weight, from_node, to_node = heapq.heappop(edges)
        if from_node not in explored and to_node not in explored:
            mst_1.append(graph.get_edge(from_node, to_node))
            explored.update([from_node, to_node])
        for edge in mst_1:
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='r', weight=edge.get_weight())

        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_edge_attributes(G,'color').values()

        nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)

        plt.pause(0.3)
    mst.extend(mst_1)
    tour = []
    tour.append(mst[0])
    mst[0] = False
    curr_node = tour[-1].get_node1().get_value()
    data = [curr_node]
    for _ in mst:
        edge = tour[-1]
        for i in range(len(mst)):
            if mst[i]:
                if curr_node in mst[i]:
                    tour.append(mst[i])
                    mst[i] = False
                    curr_node = tour[-1] - curr_node
                    data.append(curr_node)
                    break
    tour = generate_tsp_tour(data+[data[0]])
    edges = []
    total_weight = 0
    for i in range(len(tour[1:])):
        edges.append(graph.get_edge(tour[i], tour[i+1]))
        total_weight += edges[-1].get_weight()

        plt.clf()
        img = plt.imread(r'C:\Users\raufi\Downloads\Azerbaijan_adm_location_map.svg.png')  # Path to your background image
        plt.imshow(img, extent=[-4, 4, -4, 4])  # Adjust extent based on your graph coordinates
        G = nx.Graph()
        for node_key, node_value in graph.nodes.items():
            G.add_node(node_key, pos=(node_value.x, node_value.y))
        for edge in edges[:-1]:
            G.add_edge(edge.get_node1().get_value(), edge.get_node2().get_value(), color='b', weight=edge.get_weight())
        G.add_edge(edges[-1].get_node1().get_value(), edges[-1].get_node2().get_value(), color='r', weight=edges[-1].get_weight())

        pos = nx.get_node_attributes(G, 'pos')
        colors = nx.get_edge_attributes(G,'color').values()

        nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", edge_color=colors)
        if graph.is_weighted():
            labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show(block=False)

        plt.pause(0.3)

    return total_weight

def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph

if __name__ == "__main__":
    pickle_file = './data/6cities.pkl'
    graph = read_graph_from_pickle(pickle_file, 0)
    print(christofides(graph))