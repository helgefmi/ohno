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

        # Check spoilers.
        spoilers = self._get_possible_spoilers()
        self.ohno.logger.monster('Monster can be %s' % spoilers)
        self.spoiler = spoilers[0] if len(spoilers) == 1 else None
        self.ohno.logger.monster('self.spoiler is now %s' % self.spoiler)

    def __str__(self):
        return '<Monster S=%s P=%s>' % (
            self.spoiler, self.peaceful
        )
    __repr__ = __str__

    def _get_possible_spoilers(self):
        return self.ohno.spoilers.monsters.by_appearance[self.appearance]

    def monster_info(self, info):
        self.ohno.logger.monster('Got some monster_info: %s' % info)
        self.peaceful = bool(info['peaceful'])

        name = info['name']
        if name in self.ohno.spoilers.shopkeeper.all_names:
            name = 'shopkeeper'
        if name.startswith('priest of ') or name.startswith('priestess of '):
            name, _, god = name.split(' ')

        spoilers = [x for x in self._get_possible_spoilers() if x.name == name]
        assert len(spoilers) == 1, (self, self._get_possible_spoilers())
        self.spoiler = spoilers[0]
        self.ohno.logger.monster('Spoiler is %s' % self.spoiler)

    @property
    def is_peaceful(self):
        if self.peaceful is not None:
            return self.peaceful
        if self.spoiler:
            return self.spoiler.is_peaceful()
        spoilers = self._get_possible_spoilers()
        if spoilers:
            for spoiler in spoilers:
                if not spoiler.is_peaceful():
                    return False
            return True
        return None

def create(ohno, maptile):
    """Checks `maptile` for which monster to create"""
    return Monster(ohno, maptile)
