from ohno.dungeon.tile import Tile

class Level:
    def __init__(self, ohno):
        self.ohno = ohno
        self.tiles = [Tile(self.ohno, x) for x in xrange(21 * 80)]

    def update(self):
        # TODO: The way we find out of a tile has changed or not could
        #       be optimized by caching the last update in some way.
        maptiles = self.ohno.framebuffer.get_maptiles()
        for i in xrange(21 * 80):
            tile = self.tiles[i]
            maptile = maptiles[i]
            
            if tile.glyph != maptile.glyph or \
               tile.color != maptile.color:
                tile.set(maptile)

    def to_string(self, colorize=False):
        output = ''
        last = None
        for x in xrange(21 * 80):
            tile = self.tiles[x]
            if colorize and ((not last) or last.color != tile.color):
                output += '\x1b[m\x1b[%d;%dm' % (tile.color['fg'], tile.color['bg'])
                if tile.color['bold']:
                    output += '\x1b[1m'
                if tile.color['reverse']:
                    output += '\x1b[7m'
            output += tile.glyph
            if (x + 1) % 80 == 0:
                output += '\n'
            last = tile
        if colorize:
            output += '\x1b[m'

        return output
