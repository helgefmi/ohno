import re

class Item(object):
    match_appearance = re.compile("""
        ^
        (?P<qty>a|an|\d+)\s+                    # Quantity
        (?P<name>.*?)                           # Appearance
        $
    """, re.VERBOSE)

    """
    Base class for an item. (i.e. Book, Corpse, Scroll)
    """

    def __init__(self, ohno, appearance):
        self.ohno = ohno
        self.appearance = appearance

        mdict = Item.match_appearance.match(appearance).groupdict()

        self.quantity = (1 if mdict['qty'] in ['a', 'an', '1']
                           else int(mdict['qty']))
        self.spoiler = ohno.spoilers.items.get_item_by_identity(mdict['name'])

def create(ohno, appearance):
    """Checks `appearance` for which item to create"""
    return Item(ohno, appearance)
