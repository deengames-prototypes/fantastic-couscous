import pytest

from fantastic_couscous.ecs.entity import Entity

class TestEntity:
    def test_getter_gets_set_values(self):
        e = Entity()
        expected = IntComponent(13)
        e.set(expected)

        actual = e.get(IntComponent)
        assert actual == expected


class IntComponent:
    def __init__(self, value):
        self.value = value