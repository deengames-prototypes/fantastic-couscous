from ecs.bakhumri import Bakhumri


class Entity:
    def __init__(self, *components):
        self.components = {}
        Bakhumri.all_entities.append(self)

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
        Bakhumri.all_entities.remove(self)
