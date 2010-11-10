import bpython

class Input:
    def __init__(self, ohno):
        self.ohno = ohno

    def update(self):
        """Checks if the user pressed a key and acts accordingly"""
        self.ohno.logger.input('Checking for input from keyboard..')
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

