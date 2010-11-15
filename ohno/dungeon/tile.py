import string

_tile_is_feature  = lambda t: t.glyph in '.}{#_<>]^|-~ '
_tile_is_item     = lambda t: t.glyph in '`0*$[%)(/?!"=+\\'
_tile_is_monster  = lambda t: t.glyph in (string.ascii_letters + "12345@'&;:")
_tile_is_walkable = lambda t: (t.glyph in '.}{#<>^ ') or \
                              (t.glyph == '-' and t.color['fg'] == 33)

class Tile:
    def __init__(self, level, idx):
        self.level = level
        self.ohno = self.level.ohno
        self.idx = idx

        self.glyph = ' '
        self.color = {
            'fg': 37, 'bg': 40,
            'bold': False,
            'reverse': False
        }

        self.walkable = False
        self.explored = False
        self.items = []
        self.monster = None

    def set(self, maptile):
        if _tile_is_feature(maptile):
            self.explored = self.explored or maptile.glyph != ' '
            if self.items:
                self.items = []
            self.walkable = _tile_is_walkable(maptile)
        elif _tile_is_item(maptile):
            self.explored = True
            self.walkable = maptile.glyph != '0'
            self.items = [] # TODO
        elif self.idx == self.ohno.hero.get_position_idx():
            self.explored = True
            self.walkable = True
            self.monster = None # TODO
        elif _tile_is_monster(maptile):
            pass

        self.glyph = maptile.glyph
        self.color = maptile.color.copy()

    def adjacent(self):
        ret = []
        dirs = (
            (-1, -1), (-1, 0), (-1, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
            ( 0, -1), ( 0, 1)
        )
        x, y = self.idx % 80, self.idx / 80
        for (x2, y2) in ((dir[0] + x, dir[1] + y) for dir in dirs):
            if (0 <= x2 < 80) and (0 <= y2 < 80):
                ret.append(self.level.tiles[y2 * 80 + x2])
        return ret
