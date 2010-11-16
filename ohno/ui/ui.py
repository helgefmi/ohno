from ohno.ui.curses import Curses
from ohno.ui.input import Input
from ohno.ui.uimode import UIMode
from ohno.ui.normalmode import NormalMode

class UI(object):
    """The main controller of input/output from/to the user"""
    def __init__(self, ohno):
        self.ohno = ohno
        self.curses = Curses(ohno)
        self.input = Input(ohno)
        self.set_mode(NormalMode(ohno))

    def shutdown(self):
        self.curses.shutdown()

    def getch(self):
        return self.curses.getch()

    def set_mode(self, mode):
        self.ohno.logger.ui('Setting mode to %s' % mode)
        self.mode = mode

    def update(self):
        self.curses.draw_maptiles()
        self.curses.draw_botlines()
        ret = self.input.update()
        if ret is not None:
            self.set_mode(ret(self.ohno))
