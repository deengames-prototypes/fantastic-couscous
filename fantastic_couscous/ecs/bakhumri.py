class BakhumriDough:
    # Useful for Entity.get('tag'). But because of this, consumers of our ECS
    # need to call `.destroy` when they're done with entities.
    def __init__(self):
        self.all_entities = []

    def __call__(self, component_class):
        """
        Returns all entities of a specific class type (including subclasses).
        eg. if you create a Wall entity class, Entity.get_all(Wall) returns that
        instance, while Entity.get_all(Entity) returns every entity created
        (including Wall, which subclasses Entity directly or indirectly).

        eg. Bakhumri(Wall), Bakhumri(Entity)
        """
        return [e for e in self.all_entities if e.has(component_class)]

    # Used to clean up test fixtures quickly
    def reset(self):
        self.all_entities = []


Bakhumri = BakhumriDough()
