from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.systems.keyboard_input_system import KeyboardInputSystem

import pytest

class TestKeyboardInputSystem:
    def test_get_all_keys_pressed_returns_keys_from_update(self):
        kis = KeyboardInputSystem()
        assert kis.get_all_keys_pressed() == []

        # tdl.event.get() returns ["LEFT"]
        kis.update([])

        assert kis.get_all_keys_pressed() == ["LEFT"]

    def test_update_calls_keydown_callback_on_all_entities(self):
        pressed = []
        k = KeyboardInputComponent(lambda keys: pressed.extend(keys))
        e = Entity(k)

        kis = KeyboardInputSystem()
        kis.update([e])

        # tdl.event.get() returns ["LEFT"]        
        assert "LEFT" in pressed