from fantastic_couscous.ecs.systems.keyboard_input_system import KeyboardInputSystem

import pytest

class TestKeyboardInputSystem:
    def test_get_all_keys_pressed_returns_keys_from_update(self):
        kis = KeyboardInputSystem()
        assert kis.get_all_keys_pressed() == []

        # tdl.event.get() returns ["LEFT"]
        kis.update([])

        assert kis.get_all_keys_pressed() == ["LEFT"]
