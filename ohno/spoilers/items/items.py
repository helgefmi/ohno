from collections import defaultdict
import re

from ohno.spoilers.items import amulet, armor, food, gem, other, potion, \
                                ring, scroll, spellbook, tool, wand, weapon

class Items(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self._item_by_identity = dict()
        self._items_by_appearance = defaultdict(dict)
        self._identity_plurals = {}
        self._appearance_plurals = {}

        self.ohno.logger.spoilers('Initializing itemspoilers')
        for module in (amulet, armor, food, gem, other, potion, ring,
                       scroll, spellbook, tool, wand, weapon):
            if hasattr(module, 'appearance_plurals'):
                self._appearance_plurals.update(
                    getattr(module, 'appearance_plurals')()
                )

            self.ohno.logger.spoilers('Getting items from %s' % module)
            items, defaults = getattr(module, 'items')()
            for identity, itemattrs in items.iteritems():
                item = defaults.copy()
                item.update(itemattrs)

                plural = item.pop('plural', None)

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

    def _singularize_identity(self, key):
        if key in self._identity_plurals:
            return self._identity_plurals[key]
        return key

    def _simplify_appearance(self, key):
        if key in self._appearance_plurals:
            key = self._appearance_plurals[key]

        key = re.compile(' potions?$').sub('', key)
        key = re.compile('^scrolls? labeled ').sub('', key)
        key = re.compile(' spellbooks?$').sub('', key)
        key = re.compile(' rings?$').sub('', key)
        key = re.compile(' wands?$').sub('', key)

        return key

    def get_item_by_identity(self, key):
        key = self._singularize_identity(key)
        return self._item_by_identity[key]

    def get_items_by_appearance(self, key):
        key = self._simplify_appearance(key)
        return self._items_by_appearance[key]

    def discover(self, appearance, identity):
        self.ohno.logger.spoilers('Discovered %s -> %s' % (
            appearance, identity
        ))

        appearance = self._simplify_appearance(appearance)
        identity = self._singularize_identity(identity)

        item = self._item_by_identity[identity]

        assert appearance in self._items_by_appearance, appearance
        items = self._items_by_appearance[appearance]
        assert items[identity] == item

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
                if len(value) == 1:
                    discoveries[key] = value.values()[0]['name']

        # TODO: This can surely be done with scrolls, wands, and such?
        #self.ohno.logger.spoilers('%s was %s' % (
        #    appearance, ', '.join(items)
        #))
        #self._items_by_appearance[appearance] = {identity: item}

        if discoveries:
            self.ohno.logger.spoilers('New discoveries: %s' % discoveries)
            for key, value in discoveries.iteritems():
                self.discover(key, value)
