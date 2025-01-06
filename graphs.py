class Node:
    def __init__(self, name: str, node_type: str):
        self.name = name
        self.node_type = node_type


class Edge:
    def __init__(self, parent: Node, child: Node):
        self.parent = parent
        self.child = child


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, *nodes: Node):
        self.nodes.extend(nodes)

    def add_edges(self, *edges: Edge):
        self.edges.extend(edges)
