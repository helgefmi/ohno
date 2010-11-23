from ohno.dungeon.feature.basefeature import BaseFeature

class Staircase(BaseFeature):
    def __init__(self, ohno, maptile):
        super(Staircase, self).__init__(ohno, maptile)

    @property
    def direction(self):
        return 'down' if self.appearance.glyph == '>' else 'up'
