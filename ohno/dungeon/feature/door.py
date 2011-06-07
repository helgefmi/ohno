from ohno.dungeon.feature.basefeature import BaseFeature

class Door(BaseFeature):
    def __init__(self, ohno, maptile):
        super(Door, self).__init__(ohno, maptile)
        self.locked = None

    @property
    def closed(self):
        return self.appearance.glyph == ']'

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
