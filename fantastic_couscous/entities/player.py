from fantastic_couscous.ecs.components.display_component import DisplayComponent
from fantastic_couscous.ecs.components.keyboard_input_component import KeyboardInputComponent
from fantastic_couscous.ecs.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__(
            DisplayComponent('@', 0xFFFFFF, 40, 25),
            KeyboardInputComponent(self._process_input))
        
    def _process_input(self, keys_pressed):
        for key_pressed in keys_pressed:
            if key_pressed == "UP":
                self.get(DisplayComponent).y -= 1
            elif key_pressed == "DOWN":
                self.get(DisplayComponent).y += 1
            elif key_pressed == "LEFT":
                self.get(DisplayComponent).x -= 1
            elif key_pressed == "RIGHT":
                self.get(DisplayComponent).x += 1
            else:
                print("You pressed {}".format(key_pressed))