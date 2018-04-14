# A generic container of systems. This is how we define a bunch of systems.
# Singleton-ish, so it's both easily accessible and unit-testable.
class Container:

    instance = None

    def __init__(self):
        Container.instance = self
        # Add default systems
        self._systems = []
    
    def add_system(self, system):
        self._systems.append(system)
    
    def add_entity(self, entity):
        for system in self._systems:
            system.add(entity)
    
    def update(self):
        for s in self._systems:
            s.update()
