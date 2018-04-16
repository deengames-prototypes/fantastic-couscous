class DisplayComponent:
    """Add this component to entities that have coordinates, and display.
    Really, that should be almost every entity."""
    def __init__(self, character, colour, x, y):
        self.character = character
        self.colour = colour
        self.x = x
        self.y = y
