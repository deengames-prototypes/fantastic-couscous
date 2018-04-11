from fantastic_couscous.ecs.entity import Entity


class BakhumriDough:
    def __call__(self, class_to_get):
        """
        Returns all entities of a specific class type (including subclasses).
        eg. if you create a Wall entity class, Entity.get_all(Wall) returns that
        instance, while Entity.get_all(Entity) returns every entity created
        (including Wall, which subclasses Entity directly or indirectly).

        eg. Bakhumri(Wall), Bakhumri(Entity)
        """
        if issubclass(class_to_get, Entity):
            return [e for e in Entity.all_entities if issubclass(type(e), class_to_get)]
        else:
            return [e for e in Entity.all_entities if e.has(class_to_get)]

    # Used to clean up test fixtures quickly
    def reset(self):
        Entity.all_entities = []


Bakhumri = BakhumriDough()
