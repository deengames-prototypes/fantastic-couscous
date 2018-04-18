from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.systems.keyboard_input_system import KeyboardInputSystem

import tdl
import pytest

class TestKeyboardInputSystem:
    def test_keys_pressed_returns_keys_from_update(self, monkeypatch):
        kis = KeyboardInputSystem()
        assert kis._keys_pressed == []

        monkeypatch.setattr("tdl.event.get", lambda: [KeyEvent("LEFT")])
        kis.update([])

        assert kis._keys_pressed == ["LEFT"]

    def test_update_calls_keydown_callback_on_all_entities(self, monkeypatch):
        pressed = []
        k = KeyboardInputComponent(lambda keys: pressed.extend(keys))
        e = Entity(k)

        kis = KeyboardInputSystem()        
        monkeypatch.setattr("tdl.event.get", lambda: [KeyEvent("RIGHT")])
        kis.update([e])
        
        assert "RIGHT" in pressed

    @pytest.mark.parametrize("key, expected", [
        ('ESCAPE', True), ('q', True),
        ("LEFT", False), ("e", False), ("9", False)        
    ])
    def test_check_for_game_over_returns_true_for_escape_and_q(self, monkeypatch, key, expected):
        kis = KeyboardInputSystem()
        kis._keys_pressed.append(key)
        actual = kis.check_for_game_over()
        assert actual == expected
    
    @pytest.mark.parametrize("key, expected", [
        ("LEFT", True), ("RIGHT", True), ("UP", True), ("DOWN", True),
        ("ESACAPE", False), ("7", False), ("a", False)
    ])
    def test_check_if_time_passed_returns_true_for_arrow_keys(self, monkeypatch, key, expected):
        kis = KeyboardInputSystem()
        kis._keys_pressed.append(key)
        actual = kis.check_if_time_passed()
        assert actual == expected

class KeyEvent:
    def __init__(self, key, event_type="KEYDOWN"):
        self.keychar = key
        self.type = event_type