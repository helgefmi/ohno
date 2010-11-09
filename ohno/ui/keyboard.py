import bpython

class Keyboard:
    def __init__(self, ohno):
        self.ohno = ohno

    def update(self):
        self.ohno.logger.keyboard('Checking for input from keyboard..')
        """Checks if the user pressed a key"""
        input = self.ohno.ui.getch()
        if 0 < input < 255:
            input = chr(input)
            if input == '|':
                # Opens up a bpython REPL.
                embedded_locals = {
                    'ohno': self.ohno
                }
                bpython.embed(locals_=embedded_locals)
                self.ohno.ui.curses.init_colors()
            elif input == 'S':
                self.ohno.save()

