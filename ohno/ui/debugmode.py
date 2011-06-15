from __future__ import absolute_import

import curses

from ohno.ui.basemode import BaseMode

class DebugMode(BaseMode):
    """
    A UI mode used for debugging.
    Things ilke investigating tiles should be possible in this mode.
    Whenever DebugMode() is called, ohno will be set in paused mode.
    """
    def __init__(self, ohno):
        self.ohno = ohno
        # Debug cursor, for investigating tiles while the game is paused.
        self.cursor = {
            'y': self.ohno.hero.position.y,
            'x': self.ohno.hero.position.x,
        }
        self.ohno.paused = True

    def __str__(self):
        return 'debug'
    __repr__ = __str__

    def get_cursor_idx(self):
        return self.cursor['y'] * 80 + self.cursor['x']

    def on_input(self, input):
        if input in 'sp':
            return super(DebugMode, self).on_input(input)
        elif input == '|':
            tile = self.ohno.dungeon.curlevel.tiles[self.get_cursor_idx()]
            self.ohno.ui.open_console(tile=tile)
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
        return ord(tile.appearance.glyph)

    def tile_to_color(self, tile):
        color = self.ohno.ui.curses.convert_color(tile.appearance)
        idx = self.get_cursor_idx()
        if idx == tile.idx:
            color |= curses.A_REVERSE
        if tile.explored and tile.appearance.glyph == ' ':
            color |= curses.A_STANDOUT
        return color

    def first_botline(self):
        hero = self.ohno.hero
        idx = self.get_cursor_idx()
        tile = self.ohno.dungeon.curlevel.tiles[idx]

        extra = ''
        if tile.monster and tile.monster.spoiler:
            extra += ' %s P=%d' % (tile.monster.spoiler.name,
                                   tile.monster.is_peaceful)

        return '%2d,%2d W:%d R:%d E:%d F:%s I:%d M:%s A:%s S:%d Di:%s %s' % (
            self.cursor['y'], self.cursor['x'],
            tile.walkable,
            1 if tile.reachable else 0,
            tile.explored,
            tile.feature.appearance if tile.feature else '  ',
            len(tile.items),
            tile.monster.appearance if tile.monster else '  ',
            tile.appearance,
            tile.searched,
            tile.distance_from_hero(),
            extra
        )

    def second_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (
            hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level, hero.turns,
            hero.gold
        )

    def rightpane(self):
        idx = self.get_cursor_idx()
        tile = self.ohno.dungeon.curlevel.tiles[idx]
        if not tile.items:
            return super(DebugMode, self).rightpane()
        return '\n'.join(str(item) for item in tile.items)
