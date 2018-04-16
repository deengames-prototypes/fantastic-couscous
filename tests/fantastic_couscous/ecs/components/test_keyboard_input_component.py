from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent

import pytest

class TestKeyboardInputComponent:

    def test_init_takes_callback_which_accepts_keys_pressed(self):
        pressed = []
        k = KeyboardInputComponent(lambda keys: pressed.extend(keys))
        k.on_keydown_callback(["a", "b"])

        assert len(pressed) == 2
        assert "a" in pressed
        assert "b" in pressed