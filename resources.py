from constants import ResourceTypes
from graphs import Node, Edge, Graph
from identities import Binding
from resource_builders.resource_builder import ResourcesBuilder


class Resource(Node):
    def __init__(self, name: str, resource_type: ResourceTypes, *bindings: Binding):
        super().__init__(name, resource_type.value)
        self.bindings = bindings

    def __str__(self):
        return f"{self.name}({self.node_type}) bindings: [{'; '.join(map(str, self.bindings))}]"


class ResourceRelation(Edge):
    def __init__(self, parent: Resource, child: Resource):
        super().__init__(parent, child)

    def __str__(self):
        return f"{self.parent} -> {self.child}"


class ResourceGraph(Graph):
    def create_resources(self, builder: ResourcesBuilder):
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
            "folder2", ResourceTypes.folder, identity_role_binding3, identity_role_binding4
        )
        sub_folder = builder.create_resource("sub-folder", ResourceTypes.folder, identity_role_binding3)

        resource_relation1 = builder.create_resource_relation(org_folder, folder1)
        resource_relation2 = builder.create_resource_relation(org_folder, folder2)
        resource_relation3 = builder.create_resource_relation(folder1, sub_folder)

        self.add_nodes(org_folder, folder1, folder2, sub_folder)
        self.add_edges(resource_relation1, resource_relation2, resource_relation3)

    def __str__(self):
        return "\n".join([str(edge) for edge in self.edges])
