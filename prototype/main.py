import os
import sys
# import ../*
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fantastic_couscous.ecs.entity import Entity
from fantastic_couscous.ecs.components.display_component import DisplayComponent

import tdl

class Player(Entity):
    def __init__(self):
        super().__init__(DisplayComponent('@', 0xFFFFFF, 40, 25))

class Main:
    def __init__(self):
        self.player = Player()
        self.root_console = tdl.init(80, 50)
        self.game_over = False

    def core_game_loop(self):
        self.draw()

        while not tdl.event.is_window_closed() and not self.game_over:
            user_input = tdl.event.key_wait()
            key_pressed = user_input.keychar
            self.process_input(key_pressed)
            # time passes
            self.draw()
    
    def process_input(self, key_pressed):
        if key_pressed == "ESCAPE" or key_pressed == 'q':
            self.game_over = True

    def draw(self):
        dc = self.player.get(DisplayComponent)
        self.root_console.draw_char(dc.x, dc.y, dc.character, dc.colour)
            

if __name__ == "__main__":
    Main().core_game_loop()
