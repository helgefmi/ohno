import string

from ohno.dungeon.item.item import Item
from ohno.dungeon.monster.monster import Monster

from ohno.dungeon.feature import feature
from ohno.dungeon.feature.door import Door


_tile_is_feature  = lambda t: t['glyph'] in '.}{#_<>]^|-~ \\'
_tile_is_item     = lambda t: t['glyph'] in '`0*$[%)(/?!"=+'
_tile_is_monster  = lambda t: t['glyph'] in (string.ascii_letters + "12345@'&;:")
# doors are handled in walkable()
_tile_is_walkable = lambda t: (t['glyph'] in '.}{#<>^ ')

class Tile(object):
    def __init__(self, level, idx):
        self.level = level
        self.ohno = self.level.ohno
        self.idx = idx

        self._walkable = False
        self.explored = False

        self.feature = None
        self.items = []
        self.monster = None
        self.has_hero = None

        self._adjacent = None

    def set(self, maptile):
        """
        Will be called by `ohno.dungeon.level.update` if the current glyph or
        color has been changed since since the last update.
        `maptile` is "newly copied" (i.e. it's safe to change)
        """
        if _tile_is_feature(maptile):
            # Spaces ("dark part of the room") can never be set to explored
            # unless we have been adjacent to the square yet. This logic is
            # found in ohno.dungeon.level.
            self.explored = self.explored or maptile['glyph'] != ' '
            # If it's the first time we're seeing the feature of this tile or if
            # it has changed (i.e. water can spread to nearby floortiles).
            if (not self.feature) or self.feature.appearance != maptile:
                self.feature = feature.create(self, maptile)
                self._walkable = self.is_open_door() or _tile_is_walkable(maptile)
            self.items = []
            self.has_hero = False
            self.set_monster(None)
        elif _tile_is_item(maptile):
            self._walkable = True
            self.has_hero = False

            # If the appearance of the tile changes (i.e. something else
            # has dropped, or a monster picking up the topmost item),
            # we'll completely remove any previous examined items,
            # since the hero should reexamine the tile anyway.
            # If it stays the same, we'll simply assume nothing has changed.
            if (not self.items) or self.items[-1].appearance != maptile:
                self.items = [Item.create(self, maptile)]
                # Since this tile might have new information,
                # we set explored to False. That way, it'll be easier for our AI
                # to know this square is interesting.
                self.explored = False
        elif self.idx == self.ohno.hero.get_position_idx():
            self.ohno.logger.tile('Updating tile with %s: %r' % (self.ohno.hero, self))
            self._walkable = True
            self.has_hero = True
            self.set_monster(None)
            if (not self.ohno.hero.appearance) or \
               self.ohno.hero.appearance != maptile:
                # Not sure if we need this, but this seems like a good place to
                # check if we're polymorphed.
                self.ohno.hero.appearance = maptile
            self.ohno.logger.tile('Updated tile with %s: %r' % (self.ohno.hero, self))
        elif _tile_is_monster(maptile):
            # TODO: Might not be true if this is a stone giant standing on a
            #       boulder.
            self.has_hero = False
            self._walkable = True
            if (not self.monster) or self.monster.appearance != maptile:
                self.set_monster(Monster.create(self, maptile))

    # TODO: Meh, move this to the pathing code.
    #       I see no other uses for this function.
    def is_open_door(self):
        return self.feature and (self.feature.appearance['glyph'] in '-|' and self.feature.appearance['color']['fg'] == 33)

    # TODO: Meh, move this to the pathing code.
    #       I see no other uses for this function.
    def can_walk_diagonally(self):
        return not self.is_open_door()

    @property
    def walkable(self):
        # TODO: The following is not true if we're currently a giant or have
        # the ability to fly (i think :)..
        # This might be called before the tile is initialized, so make sure we
        # consider the case where appearance is None
        return self.appearance and self._walkable and self.appearance['glyph'] != '0'

    @property
    def appearance(self):
        """What does this tile look like right now?"""
        # This could be cached, but doing it like this do work as a sanity check
        # aswell :-)
        if self.monster is not None:
            return self.monster.appearance
        elif self.has_hero:
            return self.ohno.hero.appearance
        elif self.items:
            return self.items[-1].appearance
        elif self.feature is not None:
            return self.feature.appearance
        else:
            return None

    @property
    def adjacent(self):
        """Return the direct neighbors of this tile."""
        # Since ohno.dungeon.level.tiles never changes (it's even a tuple), we
        # can safely cache the result of this function the first time we run it.
        if self._adjacent is None:
            self._adjacent = []
            dirs = (
                (-1, -1), (-1, 0), (-1, 1),
                ( 1, -1), ( 1, 0), ( 1, 1),
                ( 0, -1), ( 0, 1)
            )
            x, y = self.idx % 80, self.idx / 80
            for (x2, y2) in ((dir[0] + x, dir[1] + y) for dir in dirs):
                if (0 <= x2 < 80) and (0 <= y2 < 21):
                    self._adjacent.append(self.level.tiles[y2 * 80 + x2])
            self._adjacent = tuple(self._adjacent)
        return self._adjacent

    def set_monster(self, monster):
        if self.monster is not None:
            self.level.monsters.remove(self.monster)
        self.monster = monster
        self.level.monsters.append(monster)

    # Methods for simpler API to ohno.ai.pathing.search_where
    @property
    def has_monster(self):
        return self.monster is not None

    @property
    def has_closed_door(self):
        return isinstance(self.feature, Door) and self.feature.closed

    @property
    def feature_name(self):
        return self.feature.__class__.__name__ if self.feature else 'Unknown'

    def feature_is_a(self, class_name):
        return self.feature_name == class_name

    def __str__(self):
        return '<Tile idx=%d A=%s E=%d W=%d>' % (
            self.idx, self.appearance, self.explored, int(self.walkable or 0)
        )

    def __repr__(self):
        return str(self)
