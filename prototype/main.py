import os
import sys
# import ../*
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fantastic_couscous.ecs.container import Container
from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.systems.display_system import DisplaySystem
from fantastic_couscous.ecs.components.display_component import DisplayComponent

import tdl

class Player(Entity):
    def __init__(self):
        super().__init__(DisplayComponent('@', 0xFFFFFF, 40, 25))

class Main:
    def __init__(self):
        self.player = Player()
        self.game_over = False
        
        self.container = Container()
        # Order matters. Draw last.
        self.container.add_system(DisplaySystem(tdl.init(80, 50)))
        
        self.container.add_entity(self.player)

    def core_game_loop(self):
        self.container.update()

        while not tdl.event.is_window_closed() and not self.game_over:
            user_input = tdl.event.key_wait()
            key_pressed = user_input.keychar
            self.process_input(key_pressed)
            # time passes
            self.container.update()
    
    def process_input(self, key_pressed):
        if key_pressed == "ESCAPE" or key_pressed == 'q':
            self.game_over = True
        elif key_pressed == "UP":
            self.player.get(DisplayComponent).y -= 1
        elif key_pressed == "DOWN":
            self.player.get(DisplayComponent).y += 1
        elif key_pressed == "LEFT":
            self.player.get(DisplayComponent).x -= 1
        elif key_pressed == "RIGHT":
            self.player.get(DisplayComponent).x += 1
        else:
            print("You pressed {}".format(key_pressed))


if __name__ == "__main__":
    Main().core_game_loop()
