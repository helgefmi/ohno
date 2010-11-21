import bpython

from ohno.ui.curses import Curses
from ohno.ui.normalmode import NormalMode

class UI(object):
    """The main controller of input/output from/to the user"""
    def __init__(self, ohno):
        self.ohno = ohno
        self.curses = Curses(ohno)
        self.set_mode(NormalMode(ohno))

    def shutdown(self):
        self.curses.shutdown()

    def set_mode(self, mode):
        self.ohno.logger.ui('Setting mode to %s' % mode)
        self.mode = mode

    def update(self):
        self.curses.draw_maptiles()
        self.curses.draw_botlines()

        input = self.curses.getch()
        if 0 < input < 255:
            input = chr(input).lower()
            ret = self.ohno.ui.mode.on_input(input)
            if ret is not None:
                self.set_mode(ret(self.ohno))

    def open_console(self, **kwargs):
        # Opens up a bpython REPL.
        embedded_locals = {
            'ohno': self.ohno
        }
        embedded_locals.update(kwargs)
        bpython.embed(locals_=embedded_locals)
        # Since bpython will modify our curses setup, we need to
        # reinitialize curses (nodelay, noecho, ..).
        self.ohno.ui.curses.start_curses()
