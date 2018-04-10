import pytest
import random

from fantastic_couscous.ecs.entity import Entity

class TestEntity:
    def setup(self):
        Entity.destroy_all()

    def test_getter_gets_set_values(self):
        e = Entity()
        expected = IntComponent(13)
        e.set(expected)

        actual = e.get(IntComponent)
        assert actual == expected

    def test_entity_getall_gets_all_entities_of_that_type(self):
        w1 = Wall()
        w2 = Wall()
        t = Tree()

        all_walls = Entity.get_all(Wall)
        all_trees = Entity.get_all(Tree)

        assert len(all_walls) == 2
        assert all_walls[0] == w1
        assert all_walls[1] == w2
        
        assert len(all_trees) == 1
        assert all_trees[0] == t
    
    def test_entity_getall_gets_all_subclasses_of_that_type(self):
        w = Wall()
        m = MetalWall()
        t = Tree()

        all_walls = Entity.get_all(Wall)
        assert len(all_walls) == 2
        assert all_walls[0] == w
        assert all_walls[1] == m

    def test_entity_destroy_removes_entity_from_getall(self):
        t = Tree()
        assert Entity.get_all(Tree)[0] == t
        t.destroy()

        actual = Entity.get_all(Tree)
        assert len(actual) == 0

class IntComponent:
    def __init__(self, value):
        self.value = value

class Wall(Entity):
    pass

class MetalWall(Wall):
    pass

class Tree(Entity):
    pass