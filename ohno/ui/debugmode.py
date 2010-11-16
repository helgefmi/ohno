from __future__ import absolute_import

import curses

from ohno.ui.normalmode import NormalMode

class DebugMode(NormalMode):
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
        if input in '|sp':
            return super(DebugMode, self).on_input(input)
        elif input == 'q':
            from ohno.ui.normalmode import NormalMode
            return NormalMode

        if input in 'yhb':
            self.cursor['x'] -= 1
        if input in 'bnj':
            self.cursor['y'] += 1
        if input in 'yuk':
            self.cursor['y'] -= 1
        if input in 'uln':
            self.cursor['x'] += 1

        # Make sure the cursor are within the boundaries of the width and height
        # of the tileset.
        self.cursor['x'] = min(max(0, self.cursor['x']), 79)
        self.cursor['y'] = min(max(0, self.cursor['y']), 20)

    def tile_to_glyph(self, tile):
        return ord(tile.appearance['glyph'])

    def tile_to_color(self, tile):
        color = self.ohno.ui.curses.convert_color(tile.appearance['color'])
        idx = self.get_cursor_idx()
        if idx == tile.idx:
            color |= curses.A_REVERSE
        if tile.explored and tile.appearance['glyph'] == ' ':
            color |= curses.A_STANDOUT
        return color

    def _appearance_to_str(self, appearance):
        color_str = '%d' % (appearance['color']['fg'] - 30)
        color_str += 'b' if appearance['color']['bold'] else ' '
        return '%s,%s' % (appearance['glyph'], color_str)

    def first_botline(self):
        hero = self.ohno.hero
        idx = self.get_cursor_idx()
        tile = self.ohno.dungeon.curlevel.tiles[idx]

        return 'P:%2d,%2d C:%2d,%2d(%4d) W:%d E:%d F:%s I:%d M:%s A:%s' % (
            hero.position[0], hero.position[1],
            self.cursor['y'], self.cursor['x'], idx,
            tile.walkable, tile.explored,
            self._appearance_to_str(tile.feature.appearance) if tile.feature else ' ',
            len(tile.items),
            self._appearance_to_str(tile.monster.appearance) if tile.monster else ' ',
            self._appearance_to_str(tile.appearance)
        )

    def secound_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (\
                    hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level,\
                    hero.turns, hero.gold)

    def __str__(self):
        return 'debug'
