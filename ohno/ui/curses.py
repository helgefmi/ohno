from __future__ import absolute_import

import curses

class Curses(object):
    """A class used by ohno.ui to display the current state of ohno."""
    _ansi_to_curses_colors = (
        curses.COLOR_BLACK, curses.COLOR_RED,
        curses.COLOR_GREEN, curses.COLOR_YELLOW,
        curses.COLOR_BLUE,  curses.COLOR_MAGENTA,
        curses.COLOR_CYAN,  curses.COLOR_WHITE
    )

    def __init__(self, ohno):
        """Initialises curses; remember to .shutdown()!"""
        self.ohno = ohno

        self.ohno.logger.curses('Initializing curses..')
        self._scr = curses.initscr()
        self.start_curses()

    def start_curses(self):
        """Is used to reinitialize curses after calling bpython.embed"""
        curses.start_color()
        self.init_colors()
        curses.noecho()
        curses.cbreak()
        self._scr.keypad(1)
        self._scr.nodelay(1)
        self._scr.move(0, 0)
        self._scr.clear()
        self._scr.refresh()
        self.ohno.logger.curses('Curses initialized.')

    def shutdown(self):
        """Deinitializes curses"""
        self.ohno.logger.curses('Shutting down..')
        self._scr.keypad(0)
        self._scr.nodelay(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        self.ohno.logger.curses('Curses should be deinitialized now')

    def getch(self):
        return self._scr.getch()

    def draw_maptiles(self):
        for y in xrange(21):
            for x in xrange(80):
                idx = y * 80 + x
                tile = self.ohno.dungeon.curlevel.tiles[idx]
                glyph = self.ohno.ui.mode.tile_to_glyph(tile)
                color = self.ohno.ui.mode.tile_to_color(tile)
                self._scr.addch(y, x, glyph, color)

    def draw_botlines(self):
        first = 'M:' + str(self.ohno.ui.mode)
        first += ' ' + self.ohno.ui.mode.first_botline()
        second = self.ohno.ui.mode.second_botline()

        first += ' ' * (80 - len(first))
        second += ' ' * (80 - len(second))

        self._scr.addstr(21, 0, first)
        self._scr.addstr(22, 0, second)

    @classmethod
    def convert_color(cls, appearance):
        fg = appearance.fg - 30
        return curses.color_pair(cls._ansi_to_curses_colors[fg])
    
    @classmethod
    def init_colors(cls):
        # the first pair (index 0) is hardcoded to black on black
        for x in xrange(1, 8):
            curses.init_pair(x, cls._ansi_to_curses_colors[x], 0)
