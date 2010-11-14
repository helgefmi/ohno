import bpython

from ohno.ui.uimode import UIMode

class NormalMode(UIMode):
    """
    The default mode. Every other mode should be accessable through this mode.
    """
    def __init__(self, ohno):
        self.ohno = ohno
        self.ohno.paused = False

    def on_input(self, input):
        if input == '|':
            # Opens up a bpython REPL.
            embedded_locals = {
                'ohno': self.ohno
            }
            bpython.embed(locals_=embedded_locals)
            # Since bpython will modify our curses setup, we need to
            # reinitialize curses (nodelay, noecho, ..).
            self.ohno.ui.curses.start_curses()
        elif input == 's':
            self.ohno.save()
        elif input == 'p':
            self.ohno.paused = not self.ohno.paused
        elif input == 'd':
            from ohno.ui.debugmode import DebugMode
            return DebugMode
