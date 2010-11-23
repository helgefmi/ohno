class Monster(object):
    """
    Base class for a monster.
    (i.e. Dwarf, Newt, Lich), and some common methods / attributes for all the monsters.
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which monster to create"""
        return Monster(ohno, maptile)
