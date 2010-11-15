class Feature:
    """
    Base class for a dungeon feature.
    Contains a static method to create new specific Feature instances
    (i.e. Altar, Fountain, Floor), and some common methods for all the features.
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile

    @staticmethod
    def create(ohno, maptile):
        """Checks `maptile` for which feature to create"""
        return Feature(ohno, maptile)
