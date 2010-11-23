class Item(object):
    """
    Base class for an item. (i.e. Book, Corpse, Scroll)
    """

    def __init__(self, ohno, appearance):
        self.ohno = ohno
        self.appearance = appearance

    @staticmethod
    def create(ohno, appearance):
        """Checks `appearance` for which item to create"""
        return Item(ohno, appearance)
