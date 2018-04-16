# Fakes out the TDL class so we can import/use it.
tdl_calls = []

def flush():
    tdl_calls.append("flush")

class GetEvent:
    def get(self):
        return [KeyEvent("LEFT")]

class KeyEvent:
    def __init__(self, key, event_type="KEYDOWN"):
        self.keychar = key
        self.type = event_type
        
event = GetEvent()
