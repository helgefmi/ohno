class Item(object):
    """
    Base class for an item.
    Contains a static method to create new specific Item instances
    (i.e. Book, Corpse, Scroll), and some common methods for all the items.
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which item to create"""
        return Item(ohno, maptile)
