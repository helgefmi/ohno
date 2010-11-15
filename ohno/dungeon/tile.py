import string

from ohno.dungeon.feature.feature import Feature
from ohno.dungeon.item.item import Item
from ohno.dungeon.monster.monster import Monster

_tile_is_feature  = lambda t: t['glyph'] in '.}{#_<>]^|-~ '
_tile_is_item     = lambda t: t['glyph'] in '`0*$[%)(/?!"=+\\'
_tile_is_monster  = lambda t: t['glyph'] in (string.ascii_letters + "12345@'&;:")
_tile_is_walkable = lambda t: (t['glyph'] in '.}{#<>^ ') or \
                              (t['glyph'] == '-' and t['color']['fg'] == 33)

class Tile:
    def __init__(self, level, idx):
        self.level = level
        self.ohno = self.level.ohno
        self.idx = idx

        self._walkable = False
        self.explored = False

        self.feature = None
        self.items = []
        self.monster = None

        self._adjacent = None

    def set(self, maptile):
        """
        Will be called by `ohno.dungeon.level.update` if the current glyph or
        color has been changed since since the last update.
        `maptile` is "newly copied" (i.e. it's safe to change)
        """
        if _tile_is_feature(maptile):
            self.explored = self.explored or maptile['glyph'] != ' '
            if (not self.feature) or self.feature.appearance != maptile:
                self.feature = Feature.create(self, maptile)
                self._walkable = _tile_is_walkable(maptile)
            self.items = []
            self.monster = None
        elif _tile_is_item(maptile):
            self.explored = True
            self._walkable = True

            # If the appearance of the tile changes (i.e. something else
            # has dropped, or a monster picking up the topmost item,
            # we'll completely remove any previous examined items,
            # since the hero should reexamine the tile anyway.
            # If it stays the same, we'll simply assume nothing has changed.
            if (not self.items) or self.items[-1].appearance != maptile:
                self.items = [Item.create(self, maptile)]
            self.monster = None
        elif self.idx == self.ohno.hero.get_position_idx():
            self.explored = True
            self._walkable = True
            self.monster = None
            if (not self.ohno.hero.appearance) or \
               self.ohno.hero.appearance != maptile:
                self.ohno.hero.appearance = maptile
        elif _tile_is_monster(maptile):
            self._walkable = True
            self.explored = True
            if (not self.monster) or self.monster.appearance != maptile:
                self.monster = Monster.create(self, maptile)

    @property
    def walkable(self):
        # TODO: The following is not true if we're currently a giant or have
        # the ability to fly.
        return self._walkable and self.appearance['glyph'] != '0'

    @property
    def appearance(self):
        if self.monster is not None:
            return self.monster.appearance
        elif self.idx == self.ohno.hero.get_position_idx():
            return self.ohno.hero.appearance
        elif self.items:
            return self.items[-1].appearance
        elif self.feature is not None:
            return self.feature.appearance
        else:
            return None

    @property
    def adjacent(self):
        if self._adjacent is None:
            self._adjacent = []
            dirs = (
                (-1, -1), (-1, 0), (-1, 1),
                ( 1, -1), ( 1, 0), ( 1, 1),
                ( 0, -1), ( 0, 1)
            )
            x, y = self.idx % 80, self.idx / 80
            for (x2, y2) in ((dir[0] + x, dir[1] + y) for dir in dirs):
                if (0 <= x2 < 80) and (0 <= y2 < 80):
                    self._adjacent.append(self.level.tiles[y2 * 80 + x2])
            self._adjacent = tuple(self._adjacent)
        return self._adjacent
