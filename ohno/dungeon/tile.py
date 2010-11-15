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
