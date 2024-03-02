
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.outgoing_edges = {}
        self.incoming_edges = {}
