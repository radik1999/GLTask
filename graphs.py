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

    def get_node_parent(self, node_name: str) -> Node | None:
        resource_edge = next(filter(lambda edge: edge.child.name == node_name, self.edges), None)
        if resource_edge:
            return resource_edge.parent

    def get_node_descendants(self, node_name: str) -> list[Node]:
        descendants = []

        def dfs(name: str):
            children = self.get_node_children(name)
            for child in children:
                descendants.append(child)
                dfs(child.name)

        dfs(node_name)
        return descendants

    def get_node_children(self, node_name: str) -> list[Node]:
        return [edge.child for edge in self.edges if edge.parent.name == node_name]
