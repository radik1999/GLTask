from constants import ResourceTypes
from graphs import Node, Edge, Graph
from identities import Binding
from resource_builders.resource_builder import ResourcesBuilder


class Resource(Node):
    def __init__(self, name: str, resource_type: ResourceTypes, *bindings: Binding):
        super().__init__(name, resource_type.value)
        self.bindings = bindings

    def __str__(self) -> str:
        return f"{self.name}({self.node_type}) bindings: [{'; '.join(map(str, self.bindings))}]"


class ResourceRelation(Edge):
    def __init__(self, parent: Resource, child: Resource):
        super().__init__(parent, child)

    def __str__(self) -> str:
        return f"{self.parent} -> {self.child}"


class ResourceGraph(Graph):
    def create_resources(self, builder: ResourcesBuilder) -> None:
        identity1 = builder.create_identity("user1@gmail.com")
        identity2 = builder.create_identity("user2@gmail.com")
        identity3 = builder.create_identity("user3@gmail.com")
        role1 = builder.create_role("admin")
        role2 = builder.create_role("owner")
        identity_role_binding1 = builder.create_identity_role_binding(identity1, role1)
        identity_role_binding2 = builder.create_identity_role_binding(identity2, role2)
        identity_role_binding3 = builder.create_identity_role_binding(identity2, role1)
        identity_role_binding4 = builder.create_identity_role_binding(identity3, role2)

        org_folder = builder.create_resource("org-folder", ResourceTypes.organization, identity_role_binding1)
        folder1 = builder.create_resource("folder1", ResourceTypes.folder, identity_role_binding2)
        folder2 = builder.create_resource(
            "folder2", ResourceTypes.folder, identity_role_binding3
        )
        sub_folder = builder.create_resource("sub-folder", ResourceTypes.folder, identity_role_binding4)

        resource_relation1 = builder.create_resource_relation(org_folder, folder1)
        resource_relation2 = builder.create_resource_relation(org_folder, folder2)
        resource_relation3 = builder.create_resource_relation(folder1, sub_folder)

        self.add_nodes(org_folder, folder1, folder2, sub_folder)
        self.add_edges(resource_relation1, resource_relation2, resource_relation3)

    def get_resource_parent_names(self, resource_name: str) -> list[str] | None:
        hierarchy = []

        while True:
            parent = self.get_node_parent(resource_name)
            if not parent:
                break

            parent_name = parent.name
            hierarchy.append(parent_name)
            resource_name = parent_name

        return hierarchy

    def get_user_resources(self, user_email: str) -> set[tuple[str, str, str]]:
        user_resources = [
            (node.name, node.node_type, binding.role.name)
            for node in self.nodes
            for binding in node.bindings
            if binding.user.email == user_email
        ]

        for resource in user_resources.copy():
            resource_descendants = self.get_node_descendants(resource[0])
            user_resources.extend(
                [
                    (descendant.name, descendant.node_type, resource[2])
                    for descendant in resource_descendants
                ]
            )

        return set(user_resources)

    def __str__(self) -> str:
        return "\n".join([str(edge) for edge in self.edges])
