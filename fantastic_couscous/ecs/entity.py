class Entity:

    def __init__(self):
        self.components = {}
        Entity._all_entities.append(self)
    
    def set(self, component):
        key = type(component)
        self.components[key] = component
    
    def get(self, clazz):
        return self.components[clazz]
    
    def has(self, clazz):
        return self.components[clazz] is not None

    def destroy(self):
        Entity._all_entities.remove(self)
