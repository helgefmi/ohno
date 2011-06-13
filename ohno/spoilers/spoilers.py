from ohno.spoilers.items.items import Items
from ohno.spoilers import monsters, shopkeeper

class Spoilers(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.items = Items(ohno)

        # These should be immutable anyways, don't need a class to handle any
        # state.
        self.monsters = monsters
        self.shopkeeper = shopkeeper
