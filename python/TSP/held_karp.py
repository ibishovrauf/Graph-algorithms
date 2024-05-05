from data_structures import Graph2D
import networkx as nx
from collections import defaultdict
from itertools import combinations
import pickle

def held_karp(graph: Graph2D):
    """
    Solve the Traveling Salesman Problem using the Held-Karp algorithm.
    
    :param dists: A distance matrix where dists[i][j] gives the distance between i and j.
    :return: The minimum distance to complete the tour and the path of the tour.
    """
    graph.construct_adjacency_matrix()
    dists = graph.get_adjacency_matrix()
    n = len(dists)
    # Maps each subset of the nodes to the cost to reach that subset, as well as what node it came from last
    C = {}

    # Set distance for the initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    
    # Iterate over subsets of increasing length and store the minimum distance to reach each subset
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            # Set all bits to zero except for in the subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            # Find the shortest path to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    
    # We're at the end now, so find the minimum of all paths back to 0
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    
    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    
    return opt, list(reversed(path))

def read_graph_from_pickle(pickle_file, graph):
    with open(pickle_file, 'rb') as file:
        graph = pickle.load(file)
    return graph

if __name__ == "__main__":
    pickle_file = './data/6cities.pkl'
    graph: Graph2D = read_graph_from_pickle(pickle_file, 0)
    print(held_karp(graph))