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
        self.ohno.logger.item('mdict is %s' % mdict)

        self.quantity = (1 if mdict['qty'] in ['a', 'an', '1']
                           else int(mdict['qty']))

        items = ohno.spoilers.items
        try:
            self.spoiler = items.get_item_by_identity(mdict['name'])
            self.ohno.logger.item('Spoiler: %s' % self.spoiler)
        except KeyError:
            spoilers = items.get_items_by_appearance(mdict['name'])
            self.ohno.logger.item('Spoilers: %s' % spoilers)

            if len(spoilers) == 1:
                self.spoiler = spoilers.values()[0]
                self.ohno.logger.item('Only one spoiler!')

def create(ohno, appearance):
    """Checks `appearance` for which item to create"""
    return Item(ohno, appearance)
