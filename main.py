from resource_builders.user_resource_builder import UsersResourcesBuilder
from resources import ResourceGraph

resource_grap = ResourceGraph()
builder = UsersResourcesBuilder()

resource_grap.create_resources(builder)
print(resource_grap)

resource_parent = resource_grap.get_resource_parent_names("sub-folder")
print(resource_parent)

user_resources = resource_grap.get_user_resources("user2@gmail.com")
print(user_resources)
