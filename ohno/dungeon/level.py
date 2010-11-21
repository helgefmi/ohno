from ohno.dungeon.tile import Tile

class Level(object):
    def __init__(self, ohno, dlvl):
        self.ohno = ohno
        self.dlvl = dlvl
        self.tiles = tuple(Tile(self, x) for x in xrange(21 * 80))
        self.monsters = []

    def update(self):
        self.ohno.logger.level('Updating level..')
        maptiles = self.ohno.framebuffer.get_maptiles()
        for (i, tile) in enumerate(self.tiles):
            maptile = maptiles[i]
            
            # No point in updating a tile that didn't change since last time.
            if tile.appearance != maptile:
                #self.ohno.logger.level('Updating %d: %r' % (i, tile))
                tile.set(maptile)
                #self.ohno.logger.level('RESULT:  %d: %r' % (i, tile))

        curtile = self.tiles[self.ohno.hero.get_position_idx()]
        self.ohno.logger.level('Curtile after level update %r' % curtile)
        curtile.explored = True
        
        # Since empty spaces might both be walkable and not, the only way to
        # find out (well.. at this point anyway) is to stand adjacent to the
        # square and see if it lights up (see if the glyph changes or not).
        # If it doesn't, we need to set the tile to not walkable.
        if not self.ohno.hero.blind:
            for tile in curtile.adjacent:
                if not tile.items:
                    tile.explored = True
                if tile.appearance['glyph'] == ' ':
                    tile._walkable = False
