from __future__ import absolute_import
import curses

_ansi_to_curses_colors = (
    curses.COLOR_BLACK, curses.COLOR_RED,
    curses.COLOR_GREEN, curses.COLOR_YELLOW,
    curses.COLOR_BLUE,  curses.COLOR_MAGENTA,
    curses.COLOR_CYAN,  curses.COLOR_WHITE
)

def _convert_color(color):
    fg = color['fg'] - 30
    return curses.color_pair(_ansi_to_curses_colors[fg])

class Curses:
    def __init__(self, ohno):
        self.ohno = ohno

        self.ohno.logger.curses('Initializing curses..')
        self._scr = curses.initscr()
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
        self.ohno.logger.curses('Shutting down..')
        self._scr.keypad(0)
        self._scr.nodelay(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        self.ohno.logger.curses('Curses should be deinitialized now')

    def init_colors(self):
        # the first pair (index 0) is hardcoded to black on black
        for x in xrange(1, 8):
            curses.init_pair(x, _ansi_to_curses_colors[x], 0)

    def refresh(self):
        return self._scr.refresh()

    def getch(self):
        return self._scr.getch()

    def draw_maptiles(self):
        self.ohno.logger.curses('Drawing map tiles..')
        for y in xrange(21):
            for x in xrange(80):
                idx = y * 80 + x
                tile = self.ohno.dungeon.curlevel.tiles[idx]
                self._scr.addch(y, x, ord(tile.glyph), _convert_color(tile.color))

    def draw_botlines(self):
        self.ohno.logger.curses('Drawing bottomlines..')
        hero = self.ohno.hero
        first = 'P:%2d,%2d' % (hero.position[0], hero.position[1])
        secound = 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (hero.dlvl, hero.hp, hero.hpmax, hero.ac, hero.level, hero.turns, hero.gold)

        self._scr.addstr(21, 0, first)
        self._scr.addstr(22, 0, secound)
