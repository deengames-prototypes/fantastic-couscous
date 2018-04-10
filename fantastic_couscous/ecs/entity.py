class Entity:

    # Useful for Entity.get('tag'). But because of this, consumers of our ECS
    # need to call `.destroy` when they're done with entities.
    _all_entities = []

    def __init__(self):
        self.components = {}
        Entity._all_entities.append(self)
    
    def set(self, component):
        key = type(component)
        self.components[key] = component
    
    def get(self, clazz):
        return self.components[clazz]

    def destroy(self):
        Entity._all_entities.remove(self)

    """
    Returns all entities of a specific class type (including subclasses).
    eg. if you create a Wall entity class, Entity.get_all(Wall) returns that
    instance, while Entity.get_all(Entity) returns every entity created
    (including Wall, which subclasses Entity directly or indirectly).
    """
    @staticmethod
    def get_all(clazz):
        return [e for e in Entity._all_entities if isinstance(e, clazz)]
    
    # Used to clean up test fixtures quickly
    @staticmethod
    def destroy_all():
        Entity._all_entities = []