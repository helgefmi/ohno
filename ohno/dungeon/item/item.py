class Item(object):
    """
    Base class for an item. (i.e. Book, Corpse, Scroll)
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which item to create"""
        return Item(ohno, maptile)
