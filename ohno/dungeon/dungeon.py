from ohno.dungeon.level import Level

class Dungeon:
    def __init__(self, ohno):
        self.ohno = ohno
        self.levels = {}
        self.curlevel = None
        self.curtile = None

    def update(self):
        """
        1. Check if we're on a new level, and make on if we are
        2. Set self.curlevel and self.curtile, and update the current level
        """
        # TODO: Branches. We need to know which branch we are in and which
        #       levels are in which branch.
        #       This should probably be done inside this function, while
        #       the detection code should be in Level.
        dlvl = self.ohno.hero.dlvl
        if dlvl not in self.levels:
            self.ohno.logger.dungeon('Found new level (dlvl %d)!' % dlvl)
            self.levels[dlvl] = Level(self.ohno)
            self.curlevel = self.levels[dlvl]
        self.curlevel.update()

        idx = self.ohno.hero.get_position_idx()
        self.curtile = self.curlevel.tiles[idx]

        # Make sure the cursor is right..
        assert self.curtile.glyph == self.ohno.hero.glyph
        # Sanity check
        assert self.curtile.idx == idx
