from fantastic_couscous.ecs.container import Container
from fantastic_couscous.ecs.entity import Entity

import pytest

class TestContainer:
    def test_add_system_adds_systems(self):
        s1 = DummySystem()
        s2 = DummySystem()
        c = Container()
        c.add_system(s1)
        
        assert s1 in c._systems
        assert s2 not in c._systems
    
    def test_add_entity_adds_it_to_entities(self):
        e = Entity()
        c = Container()
        c.add_entity(e)

        assert e in c.entities

    def test_update_calls_update_on_all_systems(self):
        c = Container()
        s1 = DummySystem()
        c.add_system(s1)
        c.update()

        s2 = DummySystem()
        c.add_system(s2)
        c.update()

        assert s1.update_calls == 2
        assert s2.update_calls == 1

class DummySystem:
    def __init__(self):
        self.update_calls = 0
    
    def update(self, entities):
        self.update_calls += 1