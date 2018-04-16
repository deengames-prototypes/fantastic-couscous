import os
import sys
# import ../*
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fantastic_couscous.ecs.container import Container
from fantastic_couscous.ecs.systems.display_system import DisplaySystem
from fantastic_couscous.ecs.systems.keyboard_input_system import KeyboardInputSystem

from player import Player
import tdl

class Main:
    def __init__(self):
        self.player = Player()
        self.game_over = False
        
        # We need a reference so we can draw even if there's no input (realtime)
        self.display_system = DisplaySystem(tdl.init(80, 50))
        # Needed so we can detect game-over and tell if time passed
        self.keyboard_input_system = KeyboardInputSystem()

        self.container = Container()

        # Order matters. Draw last.
        self.container.add_system(self.keyboard_input_system)
        self.container.add_system(self.display_system)
        
        self.container.add_entity(self.player)

    def core_game_loop(self):
        self.container.update()

        while not self.game_over:
            self.check_for_game_over()
            time_passed = self.check_if_time_passed()

            if time_passed:
                self.container.update()
            else:
                self.keyboard_input_system.update(self.container.entities)
                self.display_system.update(self.container.entities)
    
    def check_for_game_over(self):
        keys_pressed = [e for e in self.keyboard_input_system.get_all_keys_pressed() if e == 'ESCAPE' or e == 'q']
        if len(keys_pressed) > 0:
            self.game_over = True
    
    def check_if_time_passed(self):
        all_keys_pressed = self.keyboard_input_system.get_all_keys_pressed()

        keys_pressed = [e for e in all_keys_pressed
            if e == 'UP' or e == 'DOWN' or e == 'LEFT' or e == 'RIGHT']

        return keys_pressed # len > 0
        
        

if __name__ == "__main__":
    Main().core_game_loop()
