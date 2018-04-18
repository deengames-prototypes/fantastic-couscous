from fantastic_couscous.ecs.components.display_component import DisplayComponent
from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
from fantastic_couscous.entities.player import Player
import pytest

class TestPlayer:
    def test_initializer_adds_required_components(self):
        p = Player()
        assert p.has(DisplayComponent)
        assert p.has(KeyboardInputComponent)

    def test_process_input_moves_display_component_for_arrow_keys(self):
        p = Player()
        display = p.get(DisplayComponent)
        old_x, old_y = display.x, display.y

        p._process_input(["UP"])
        assert display.x == old_x
        assert display.y == old_y - 1
        old_x, old_y = display.x, display.y
        
        p._process_input(["DOWN"])
        assert display.x == old_x
        assert display.y == old_y + 1
        old_x, old_y = display.x, display.y

        p._process_input(["LEFT"])
        assert display.x == old_x - 1
        assert display.y == old_y
        old_x, old_y = display.x, display.y
    
        p._process_input(["RIGHT"])
        assert display.x == old_x + 1
        assert display.y == old_y