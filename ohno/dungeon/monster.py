from ohno.spoilers import monsters

class Monster(object):
    """
    Represents a monster on a tile.
    """

    def __init__(self, tile, maptile):
        self.ohno = tile.ohno
        self.tile = tile
        self.appearance = maptile

        self.spoilers = monsters.by_appearance[maptile]
        assert self.spoilers

        self.ohno.logger.monster('Found monster: %s' % self.spoilers)

    @property
    def is_peaceful(self):
        return all(x.is_peaceful() for x in self.spoilers)

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which monster to create"""
        return Monster(ohno, maptile)
