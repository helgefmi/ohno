class BaseFeature(object):
    """
    Base class for a dungeon feature.
    Contains a static method to create new specific feature instances
    (i.e. Altar, Fountain, Floor), and some common methods for all the features.
    """

    def __init__(self, ohno, maptile):
        self.ohno = ohno
        self.appearance = maptile
