from ohno.appearance import PIT
from ohno.dungeon.feature.basefeature import BaseFeature

class Trap(BaseFeature):
    def __init__(self, ohno, appearance):
        super(Trap, self).__init__(ohno, appearance)

    def is_pit(self):
        return self.appearance == PIT
