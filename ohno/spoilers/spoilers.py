from ohno.spoilers.items.items import Items
from ohno.spoilers import monsters, shopkeeper

class Spoilers(object):
    def __init__(self, ohno):
        self.ohno = ohno

        self.monsters = monsters
        self.shopkeeper = shopkeeper
        self.items = Items(ohno, self)
