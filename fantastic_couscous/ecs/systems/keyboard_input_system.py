from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
import tdl

class KeyboardInputSystem:

    def __init__(self):
        self.keys_pressed = []

    def update(self, entities):
        current_keys_pressed = []

        # Check if there's input
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                current_keys_pressed.append(event.keychar)
        
        # TODO: key_onpress, key_onrelease is now possible
        self.keys_pressed = current_keys_pressed
                
        if self.keys_pressed:
            for e in entities:
                if e.has(KeyboardInputComponent):
                    ki = e.get(KeyboardInputComponent)
                    ki.on_keydown_callback(self.keys_pressed)
    
    def get_all_keys_pressed(self):
       return self.keys_pressed