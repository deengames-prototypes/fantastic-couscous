from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.bakhumri import Bakhumri


class TestBakhumri:

    def setup(self):
        Bakhumri.reset()
    
    def test_dunder_call_gets_all_entities_of_that_type(self):
        w1 = Wall()
        w2 = Wall()
        t = Tree()

        all_walls = Bakhumri(Wall)
        all_trees = Bakhumri(Tree)

        assert len(all_walls) == 2
        assert all_walls[0] == w1
        assert all_walls[1] == w2
        
        assert len(all_trees) == 1
        assert all_trees[0] == t
    
    def test_dunder_call_gets_all_subclasses_of_that_type(self):
        w = Wall()
        m = MetalWall()
        t = Tree()

        all_walls = Bakhumri(Wall)
        assert len(all_walls) == 2
        assert all_walls[0] == w
        assert all_walls[1] == m

    def test_entity_destroy_removes_entity_from_dunder_call(self):
        t = Tree()
        assert Bakhumri(Tree)[0] == t
        t.destroy()

        actual = Bakhumri(Tree)
        assert len(actual) == 0


class Wall(Entity):
    pass


class MetalWall(Wall):
    pass


class Tree(Entity):
    pass
