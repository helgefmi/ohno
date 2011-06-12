from ohno.spoilers import monsters
from ohno.spoilers import shopkeeper

class Monster(object):
    """
    Represents a monster on a tile.
    """

    def __init__(self, tile, maptile):
        self.ohno = tile.ohno
        self.tile = tile
        self.appearance = maptile

        # Means we haven't explicitly checked yet.
        self.peaceful = None
        self.spoilers = monsters.by_appearance[maptile]
        self.ohno.logger.monster('Found spoiler: %s' % self.spoilers)

        if str(maptile) not in ['I7', 'X7', 'm4']:
            assert self.spoilers, maptile

    def __str__(self):
        return '<Monster S=%s P=%s>' % (
            self.spoilers, self.peaceful
        )
    __repr__ = __str__

    def monster_info(self, info):
        self.peaceful = bool(info['peaceful'])
        self.ohno.logger.monster('Is %s is peaceful? %s!' % (
            self, self.peaceful
        ))

        name = info['name']
        if name in shopkeeper.all_names:
            name = 'shopkeeper'

        if name.startswith('priest of ') or name.startswith('priestess of '):
            name, _, god = name.split(' ')

        self.spoilers = [x for x in self.spoilers if x.name == name]
        assert len(self.spoilers) == 1, self
        self.ohno.logger.monster('Spoiler is %s' % self.spoilers[0])

    @property
    def is_peaceful(self):
        if self.peaceful is not None:
            return self.peaceful
        return self.spoilers and all(x.is_peaceful() for x in self.spoilers)

def create(ohno, maptile):
    """Checks `maptile` for which monster to create"""
    return Monster(ohno, maptile)
