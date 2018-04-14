from fantastic_couscous.ecs.components.display_component import DisplayComponent
import tdl

class DisplaySystem:

    # Console is our production TDL console, or a mock.
    def __init__(self, console):
        self._entities = []
        self._root_console = console

    def add(self, entity):
        self._entities.append(entity)

    def update(self):
        # TODO: instead of this, track old positions and redraw only what changed
        self._root_console.clear()
        
        for e in self._entities:
            dc = e.get(DisplayComponent)
            self._root_console.draw_char(dc.x, dc.y, dc.character, dc.colour)
        
        tdl.flush()
