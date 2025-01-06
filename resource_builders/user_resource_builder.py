from identities import User, Role, Binding
from resource_builders.resource_builder import ResourcesBuilder
from resources import ResourceTypes, Resource, ResourceRelation


class UsersResourcesBuilder(ResourcesBuilder):
    def create_identity(self, email: str):
        return User(email)

    def create_role(self, name: str):
        return Role(name)

    def create_identity_role_binding(self, user: User, role: Role):
        return Binding(user, role)

    def create_resource(self, name: str, resource_type: ResourceTypes, *bindings: Binding):
        return Resource(name, resource_type, *bindings)

    def create_resource_relation(self, parent: Resource, child: Resource):
        return ResourceRelation(parent, child)
