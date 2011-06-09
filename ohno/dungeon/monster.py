from ohno.spoilers import monsters

class Monster(object):
    """
    Represents a monster on a tile.
    """

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which monster to create"""
        return Monster(ohno, maptile)

    def __init__(self, tile, maptile):
        self.ohno = tile.ohno
        self.tile = tile
        self.appearance = maptile

        self.spoilers = monsters.by_appearance[maptile]
        if str(maptile) != 'I7':
            assert self.spoilers, maptile
            self.ohno.logger.monster('Found spoiler: %s' % self.spoilers)

        self.peaceful = None # Means we haven't explicitly checked yet.

    def monster_info(self, info):
        if info.startswith('peaceful '):
            self.ohno.logger.monster('%s is peaceful!' % self)
            self.peaceful = True
            name = info[9:]
        else:
            self.peaceful = False
            name = info

        self.ohno.logger.monster('Inferring spoiler (%s)' % self.spoilers)
        self.spoilers = [x for x in self.spoilers if x.name == name]
        assert len(self.spoilers) == 1, self
        self.ohno.logger.monster('Spoiler is %s' % self.spoilers[0])

    @property
    def is_peaceful(self):
        if self.peaceful is not None:
            return self.peaceful
        return all(x.is_peaceful() for x in self.spoilers)

    def __str__(self):
        return '<Monster S=%s P=%s>' % (
            self.spoilers, self.peaceful
        )
    __repr__ = __str__
