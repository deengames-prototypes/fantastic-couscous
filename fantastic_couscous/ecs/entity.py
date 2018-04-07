class Entity:
    def __init__(self):
        self.components = {}
    
    def set(self, component):
        key = type(component)
        self.components[key] = component
    
    def get(self, clazz):
        return self.components[clazz]
