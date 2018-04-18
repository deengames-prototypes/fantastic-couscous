from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
import tdl

class KeyboardInputSystem:
    """Handles keyboard input. Given an entity with a KeyboardInputComponent,
    this system calls the on_keydown callback when a key is pressed."""
    def __init__(self):
        # tdl.event.get() consumes events, so we have to keep track of them internally.
        # TODO: stop eating non-keyboard events. Move this to a central place?
        self._keys_pressed = []

    def update(self, entities):
        current_keys_pressed = []

        # Check if there's input
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                current_keys_pressed.append(event.keychar)
        
        # TODO: key_onpress, key_onrelease is now possible
        self._keys_pressed = current_keys_pressed
                
        if self._keys_pressed:
            for e in entities:
                if e.has(KeyboardInputComponent):
                    ki = e.get(KeyboardInputComponent)
                    ki.on_keydown_callback(self._keys_pressed)
    
    def check_for_game_over(self):
        quit_keys_pressed = [e for e in self._keys_pressed if e == 'ESCAPE' or e == 'q']
        if quit_keys_pressed: # len > 0
            return True
        else:
            return False
    
    def check_if_time_passed(self):
        all_keys_pressed = self._keys_pressed

        keys_pressed = [e for e in all_keys_pressed
            if e == 'UP' or e == 'DOWN' or e == 'LEFT' or e == 'RIGHT']

        return keys_pressed # len > 0