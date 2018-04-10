import pytest

from fantastic_couscous.ecs.components.display_component import DisplayComponent

class TestDisplayComponent:
    def test_initializer_values_dont_have_validation(self):
        expected_colour = (-1, 25555, 37.0)
        d = DisplayComponent('?', expected_colour, -17.3, 'a')
        assert d.character == '?'
        assert d.colour == expected_colour
        assert d.x == -17.3
        assert d.y == 'a'