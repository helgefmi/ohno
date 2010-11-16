import bpython

class Input(object):
    def __init__(self, ohno):
        self.ohno = ohno

    def update(self):
        """Checks if the user pressed a key and acts accordingly"""
        input = self.ohno.ui.getch()
        if 0 < input < 255:
            input = chr(input).lower()
            return self.ohno.ui.mode.on_input(input)
