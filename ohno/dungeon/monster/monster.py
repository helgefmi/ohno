class Monster:
    """
    Base class for a monster.
    Contains a static method to create new specific Monster instances
    (i.e. Dwarf, Newt, Lich), and some common methods for all the monsters.
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which monster to create"""
        return Monster(ohno, maptile)
