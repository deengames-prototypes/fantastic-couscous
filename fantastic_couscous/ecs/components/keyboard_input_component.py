class KeyboardInputComponent:
    """Add this component to entities that need to track keyboard input."""
    def __init__(self, on_keydown_callback):
        """on_keypress_callback should accept an argument for the keys pressed."""
        self.on_keydown_callback = on_keydown_callback