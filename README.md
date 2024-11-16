
# Graph Algorithms

This repository contains an implementation of various graph algorithms, data structures, and related utilities in Python. It is designed to be modular, easy to understand, and extendable for educational and practical purposes.

## Features

- **Data Structures**: 
  - `Graph`: A versatile graph data structure supporting directed and undirected graphs.
  - `Edge`: Representation of graph edges with weights.
  - `Node`: Representation of graph nodes.
  - `PriorityQueue`: A utility structure for algorithms like Dijkstra's.
  
- **Graph Algorithms**:
  - Dijkstra's Shortest Path Algorithm
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Utility functions for graph traversal and manipulation

- **Visualization**: 
  - Tools to visualize graph structures and algorithmic processes.

- **Examples**:
  - Ready-to-run scripts demonstrating Dijkstra's algorithm and graph creation.

- **Testing**:
  - Unit tests for algorithms to ensure correctness and reliability.

## Directory Structure

```
Graph-algorithms-main/
├── python/
│   ├── data_structures/
│   │   ├── Edge.py
│   │   ├── Graph.py
│   │   ├── Node.py
│   │   ├── PriorityQueue.py
│   │   └── __init__.py
│   ├── algorithms/
│   │   ├── dijkstra.py
│   │   ├── depth_first_search.py
│   │   ├── breadth_first_search.py
│   │   ├── utils.py
│   │   └── __init__.py
│   ├── visulization/
│   │   ├── main.py
│   │   ├── utils.py
│   │   └── __init__.py
│   ├── examples/
│   │   ├── dijkstra.py
│   │   ├── graph.py
│   ├── tests/
│   │   ├── test_breadth_first_search.py
│   │   ├── test_depth_first_search.py
│   ├── data/
│       └── test.pkl
```

## How to Use

1. **Clone the Repository**:
   ```
   git clone https://github.com/your_username/Graph-algorithms.git
   cd Graph-algorithms-main/python
   ```

2. **Run Examples**:
   Example scripts are in the `examples/` directory. You can run them to see graph algorithms in action.
   ```
   python examples/dijkstra.py
   ```

3. **Run Tests**:
   Ensure all tests pass to verify the implementation.
   ```
   python -m unittest discover -s tests
   ```

4. **Visualize Graphs**:
   Use the tools in the `visulization/` directory to generate and display graphs.

## Requirements

- Python 3.7 or higher
- Dependencies (install using `pip`):
  ```
  pip install -r requirements.txt
  ```

## Contribution

Feel free to fork this repository, add features or algorithms, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Authors

Rauf Ibishov, Rita Gayitmazova
University Project  
