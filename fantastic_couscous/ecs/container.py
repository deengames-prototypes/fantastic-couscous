# A generic container of systems. This is how we define a bunch of systems.
# Singleton-ish, so it's both easily accessible and unit-testable.
class Container:

    instance = None

    def __init__(self):
        Container.instance = self
        self._systems = []
        self.entities = []
    
    def add_system(self, system):
        self._systems.append(system)

    def add_entity(self, entity):
        self.entities.append(entity)
    
    def update(self):
        for s in self._systems:
            s.update(self.entities)
