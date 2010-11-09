class Tile:
    def __init__(self, ohno, idx):
        self.ohno = ohno
        self.idx = idx

        self.glyph = ' '
        self.color = {
            'fg': 37, 'bg': 40,
            'bold': False,
            'reverse': False
        }

    def set(self, maptile):
        self.glyph = maptile.glyph
        self.color = maptile.color.copy()
