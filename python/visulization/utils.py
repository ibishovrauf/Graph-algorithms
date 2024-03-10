import pickle

def save_graph(graph, filename):
    with open("./data/" + filename, 'wb') as f:
        pickle.dump(graph, f)
    return "./data/" + filename
