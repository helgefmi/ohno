from ohno.ui.curses import Curses
from ohno.ui.keyboard import Keyboard

class UI:
    def __init__(self, ohno):
        self.ohno = ohno
        self.curses = Curses(ohno)
        self.keyboard = Keyboard(ohno)

    def shutdown(self):
        self.curses.shutdown()

    def getch(self):
        return self.curses.getch()

    def update(self):
        self.curses.draw_maptiles()
        self.curses.draw_botlines()
        self.curses.refresh()
        self.keyboard.update()
