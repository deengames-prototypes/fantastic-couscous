class Entity:
    # Useful for Entity.get('tag'). But because of this, consumers of our ECS
    # need to call `.destroy` when they're done with entities.
    all_entities = []

    def __init__(self, *components):
        self.components = {}
        Entity.all_entities.append(self)

        for component in components:
            self.set(component)
    
    def set(self, component):
        key = type(component)
        self.components[key] = component
    
    def get(self, clazz):
        return self.components[clazz]
    
    def has(self, clazz):
        return self.components.get(clazz, None) is not None

    def destroy(self):
        Entity.all_entities.remove(self)
