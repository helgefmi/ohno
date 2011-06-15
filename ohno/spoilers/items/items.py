from collections import defaultdict
import re

from ohno.event.discovery import Discovery
from ohno.spoilers.items import amulet, armor, food, gem, other, potion, \
                                ring, scroll, spellbook, tool, wand, weapon

class Items(object):
    def __init__(self, ohno, spoilers):
        """
        This will iterate through all the item spoilers
        (found in ohno/spoilers/items/*.py), and add the items to
        _item_by_identity and _items_by_appearance.
        """
        Discovery.subscribe(self.on_discovery)
        self.ohno = ohno

        # Maps identity (string) to item (dict).
        self._item_by_identity = dict()
        # Maps appearance (string) to a list of items.
        self._items_by_appearance = defaultdict(dict)
        # Some dicts to make it easier to lookup raw strings.
        self._identity_plurals = {}
        self._appearance_plurals = {}

        self.ohno.logger.spoilers('Initializing itemspoilers')
        for module in (amulet, armor, food, gem, other, potion, ring,
                       scroll, spellbook, tool, wand, weapon):
            if hasattr(module, 'appearance_plurals'):
                self._appearance_plurals.update(
                    getattr(module, 'appearance_plurals')()
                )

            items, defaults = getattr(module, 'items')(spoilers)
            self.ohno.logger.spoilers('Getting %d items from %s' % (
                len(items), module)
            )

            for identity, itemattrs in items.iteritems():
                # The items are simply stored in a dict.
                item = defaults.copy()
                item.update(itemattrs)

                plural = item.pop('plural', None)

                # An item can have a single appearance, or several. We'll just
                # store them in `appearances` if there are any.
                appearances = []
                if 'appearance' in item:
                    appearances.append(item.pop('appearance'))
                appearances.extend(item.pop('appearances', []))

                item['type'] = module.__name__.split('.')[-1]
                item['name'] = identity

                self._item_by_identity[identity] = item

                for appearance in appearances:
                    self._items_by_appearance[appearance][identity] = item

                if plural is not None:
                    self._identity_plurals[plural] = identity

        # Sanity check.
        for _, items in self._items_by_appearance.iteritems():
            curtype = None
            for _, item in items.iteritems():
                if curtype is None: curtype = item['type']
                assert curtype == item['type']

    def _singularize_identity(self, key):
        if key in self._identity_plurals:
            return self._identity_plurals[key]
        return key

    def _simplify_appearance(self, key):
        """
        Simplifies an appearance, since we only use the simplest possible form
        in _items_by_appearance.
        E.g. go from "fizzy potions" to "fizzy".
        """
        if key in self._appearance_plurals:
            key = self._appearance_plurals[key]

        key = key.replace('wands', 'wand')
        key = key.replace('spellbooks', 'spellbook')
        key = key.replace('scrolls', 'scroll')
        key = key.replace('rings', 'ring')
        key = key.replace('potions', 'potion')
        key = key.replace('amulets', 'amulet')

        return key

    def get_item_by_identity(self, key):
        key = self._singularize_identity(key)
        return self._item_by_identity[key]

    def get_items_by_appearance(self, key):
        key = self._simplify_appearance(key)
        return self._items_by_appearance[key]

    def discover(self, appearance, identity):
        """
        This will let us know that we have found out that `identity` has been
        given `appearance` as appearance in this game.
        This can be useful since we'll eliminate `identity` from all the other
        potential appearances, and might find new discoveries in the process
        (i.e. after we remove `identity` from an appearance, if that appearance
        only have one possibility left, we can be sure the possiblity maps to
        that appearance).
        """

        self.ohno.logger.spoilers('Discovered %s -> %s' % (
            appearance, identity
        ))

        appearance = self._simplify_appearance(appearance)
        identity = self._singularize_identity(identity)

        item = self._item_by_identity[identity]

        assert appearance in self._items_by_appearance, appearance
        items = self._items_by_appearance[appearance]
        assert items[identity] == item

        # iterate through our current appearance/item dict and remove the newly
        # discovered item from all non-matching appearance.
        # Also check for new appearances in the process.
        discoveries = {}
        for key, value in self._items_by_appearance.iteritems():
            if key == appearance:
                continue
            if identity in value:
                del value[identity]
                self.ohno.logger.spoilers('Removing %s from %s' % (
                    identity, key
                ))
                assert len(value) > 0
                # Check if the appearance can only map to one item.
                if len(value) == 1:
                    discoveries[key] = value.values()[0]['name']

        # TODO: This can surely be done with scrolls, wands, and such?
        #self.ohno.logger.spoilers('%s was %s' % (
        #    appearance, ', '.join(items)
        #))
        #self._items_by_appearance[appearance] = {identity: item}

        # If we found new discoveries during the above block of code, recurse
        # this function with those.
        if discoveries:
            self.ohno.logger.spoilers('New discoveries: %s' % discoveries)
            for key, value in discoveries.iteritems():
                self.discover(key, value)

    def on_discovery(self, event):
        self.discover(event.appearance, event.identity)
