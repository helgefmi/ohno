from __future__ import absolute_import

import curses

from ohno.ui.uimode import UIMode

class DebugMode(UIMode):
    """
    A UI mode used for debugging.
    Things ilke investigating tiles should be possible in this mode.
    Whenever DebugMode() is called, ohno will be set in paused mode.
    """
    def __init__(self, ohno):
        self.ohno = ohno
        y, x = self.ohno.hero.position
        # Debug cursor, for investigating tiles while the game is paused.
        self.cursor = {
            'y': y,
            'x': x
        }
        self.ohno.paused = True

    def get_cursor_idx(self):
        return self.cursor['y'] * 80 + self.cursor['x']

    def on_input(self, input):
        if input == '|':
            super(DebugMode, self).on_input(input)
        elif input == 's':
            self.ohno.save()
        elif input == 'p':
            self.ohno.paused = not self.ohno.paused
        elif input == 'q':
            from ohno.ui.normalmode import NormalMode
            return NormalMode
        elif input == 'h':
            self.cursor['x'] -= 1
        elif input == 'j':
            self.cursor['y'] += 1
        elif input == 'k':
            self.cursor['y'] -= 1
        elif input == 'l':
            self.cursor['x'] += 1

        # Make sure the cursor are within the boundaries of the width and height
        # of the tileset.
        self.cursor['x'] = min(max(0, self.cursor['x']), 79)
        self.cursor['y'] = min(max(0, self.cursor['y']), 20)

    def tile_to_glyph(self, tile):
        return ord(tile.glyph)

    def tile_to_color(self, tile):
        color = self.ohno.ui.curses.convert_color(tile.color)
        idx = self.get_cursor_idx()
        if idx == tile.idx:
            color |= curses.A_REVERSE
        return color

    def first_botline(self):
        hero = self.ohno.hero
        idx = self.get_cursor_idx()
        tile = self.ohno.dungeon.curlevel.tiles[idx]
        color_str = '%d' % (tile.color['fg'] - 37)
        if tile.color['bold']:
            color_str += 'b'
        if tile.color['reverse']:
            color_str += 'r'
        return 'P:%2d,%2d C:%2d,%2d(%4d) G:%s C:%s' % (\
                    hero.position[0], hero.position[1], self.cursor['y'],\
                    self.cursor['x'], idx, tile.glyph, color_str)

    def secound_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (\
                    hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level,\
                    hero.turns, hero.gold)
