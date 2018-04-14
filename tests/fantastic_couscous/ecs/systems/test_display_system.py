from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.systems.display_system import DisplayComponent
from fantastic_couscous.ecs.systems.display_system import DisplaySystem

import tdl
import pytest

class TestDisplaySystem:
    def test_init_injects_root_console(self):
        console = 37
        d = DisplaySystem(console)
        assert d._root_console == console
    
    def test_add_adds_entity(self):
        e = Entity
        d = DisplaySystem("hi")
        d.add(e)
        
        assert e in d._entities
    
    def test_update_calls_draw_char_on_console_with_display_component_from_entity(self):
        player = Entity()
        player.set(DisplayComponent('@', "white", 28, 10))

        monster = Entity()
        monster.set(DisplayComponent('m', "green", 30, 8))

        console = FakeConsole()
        ds = DisplaySystem(console)
        ds.add(player)
        ds.add(monster)

        # Act
        ds.update()

        # Assert
        pd = player.get(DisplayComponent)
        md = monster.get(DisplayComponent)
        calls = console.draw_calls
        assert calls[0] == "clear"
        assert calls[1] == "draw_char({}, {}, {}, {})".format(pd.x, pd.y, pd.character, pd.colour)
        assert calls[2] == "draw_char({}, {}, {}, {})".format(md.x, md.y, md.character, md.colour)
        assert tdl.tdl_calls[0] == "flush"

class FakeConsole:
    def __init__(self):
        self.draw_calls = []

    def clear(self):
        self.draw_calls.append("clear")

    def draw_char(self, x, y, character, colour):
        self.draw_calls.append("draw_char({}, {}, {}, {})".format(x, y, character, colour))
