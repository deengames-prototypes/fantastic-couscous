class Bakhumri:
    # Useful for Entity.get('tag'). But because of this, consumers of our ECS
    # need to call `.destroy` when they're done with entities.
    _all_entities = []

    """
    Returns all entities of a specific class type (including subclasses).
    eg. if you create a Wall entity class, Entity.get_all(Wall) returns that
    instance, while Entity.get_all(Entity) returns every entity created
    (including Wall, which subclasses Entity directly or indirectly).
    
    eg. Bakhumri(Wall), Bakhumri(Entity)
    """
    @staticmethod
    def __call__(component_class):
        return [e for e in Bakhumri._all_entities if e.has(component_class)]

    # Used to clean up test fixtures quickly
    @staticmethod
    def reset():
        Bakhumri._all_entities = []