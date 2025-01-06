from resource_builders.user_resource_builder import UsersResourcesBuilder
from resources import ResourceGraph

resource_grap = ResourceGraph()
builder = UsersResourcesBuilder()

resource_grap.create_resources(builder)

print(resource_grap)
