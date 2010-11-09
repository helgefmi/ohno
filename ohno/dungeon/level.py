from ohno.dungeon.tile import Tile

class Level:
    def __init__(self, ohno):
        self.ohno = ohno
        self.tiles = [Tile(self.ohno, x) for x in xrange(21 * 80)]

    def update(self):
        # TODO: The way we find out if a tile has changed or not could
        #       be optimized by caching the last update in some way.
        #       Let's not do that for a while, though..
        maptiles = self.ohno.framebuffer.get_maptiles()
        for i in xrange(21 * 80):
            tile = self.tiles[i]
            maptile = maptiles[i]
            
            if tile.glyph != maptile.glyph or \
               tile.color != maptile.color:
                tile.set(maptile)
