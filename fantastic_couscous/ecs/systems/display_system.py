from fantastic_couscous.ecs.components.display_component import DisplayComponent
import tdl

class DisplaySystem:

    # Console is our production TDL console, or a mock.
    def __init__(self, console):
        self._root_console = console

    def update(self, entities):
        # TODO: instead of this, track old positions and redraw only what changed
        self._root_console.clear()
        
        for e in entities:
            dc = e.get(DisplayComponent)
            self._root_console.draw_char(dc.x, dc.y, dc.character, dc.colour)
        
        tdl.flush()
