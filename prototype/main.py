import tdl

class Main:
    def __init__(self):
        pass

    def core_game_loop(self):
        root_console = tdl.init(80, 25)

        while not tdl.event.is_window_closed():
            user_input = tdl.event.key_wait()
            key_pressed = user_input.keychar
            if key_pressed == "ESCAPE" or key_pressed == 'q':
                break # game over
            

if __name__ == "__main__":
    Main().core_game_loop()