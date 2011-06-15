import string

from queryable import queryable

from ohno.dungeon import monster
from ohno.dungeon.feature import feature

_tile_is_feature  = lambda t: t.glyph in '.}{#_<>]^|-~ \\'
_tile_is_item     = lambda t: t.glyph in '`0*$[%)(/?!"=+'
_tile_is_monster  = lambda t: t.glyph in (string.ascii_letters + "12345@'&;:")
# doors are handled in walkable()
_tile_is_walkable = lambda t: t.glyph in '.}{#<>^ '

class Tile(object):
    def __init__(self, level, idx):
        self.level = level
        self.ohno = self.level.ohno
        self.idx = idx

        self._walkable = False
        self.explored = False
        self.searched = 0

        self.appearance = None
        self.feature = None
        self.monster = None
        self.items = []
        self.has_hero = None
        self.has_items = None
        self.dirty_items = None
        self.topmost_item_appearance = None

        self._adjacent = None
        self._orthogonal = None
        self._horizontal = None
        self._vertical = None

    def __str__(self):
        return '<Tile %d G=%s E=%d W=%d S=%d D=%f>' % (
            self.idx,
            self.appearance.glyph if self.appearance else ' ',
            self.explored,
            int(self.walkable or 0),
            self.searched,
            self.distance_from_hero() if self.ohno.ai.pathing.is_uptodate()
                                      else -1
        )
    __repr__ = __str__

    def set(self, appearance):
        """
        Will be called by `ohno.dungeon.level.update` if the current glyph or
        color has been changed since since the last update.
        `appearance` is "newly copied" (i.e. it's safe to change)
        """
        assert self.appearance != appearance
        self.appearance = appearance
        if _tile_is_feature(appearance):
            # If it's the first time we're seeing the feature of this tile or if
            # it has changed (i.e. water can spread to nearby floortiles).
            if not self.feature or self.feature.appearance != appearance:
                self.set_feature(appearance)

            # Spaces ("dark part of the room") can never be set to explored
            # unless we have been adjacent to the square yet. This logic is
            # found in ohno.dungeon.level.
            self.explored = self.explored or appearance.glyph != ' '

            self.has_items = False
            self.has_hero = False
            self.set_monster(None)
        elif _tile_is_item(appearance):
            # If the appearance of the tile changes (i.e. something else
            # has dropped, or a monster picking up the topmost item),
            # we'll set the dirty_items to True.
            # If it stays the same, we'll simply assume nothing has changed.
            if self.topmost_item_appearance != appearance:
                self.ohno.logger.tile('Items has changed on %s' % self)
                self.dirty_items = True
                self.topmost_item_appearance = appearance

            self._walkable = True
            self.has_hero = False
            self.has_items = True
            self.set_monster(None)

        elif self == self.ohno.dungeon.curtile:
            if self.ohno.hero.appearance != appearance:
                # Not sure if we need this, but this seems like a good place to
                # check if we're polymorphed.
                self.ohno.hero.set_appearance(appearance)

            self._walkable = True
            self.has_hero = True
            self.set_monster(None)

        elif _tile_is_monster(appearance):
            if not self.monster or self.monster.appearance != appearance:
                self.ohno.logger.tile('New monster at %s' % self)
                self.set_monster(appearance)
            self._walkable = True
            self.has_hero = False

        # Sanity check
        if self.monster is not None:
            assert appearance == self.monster.appearance
        elif self.has_hero:
            assert appearance == self.ohno.hero.appearance
        elif self.has_items:
            assert appearance == self.topmost_item_appearance
        elif self.feature is not None:
            assert appearance == self.feature.appearance
        else:
            assert False

    def set_feature(self, appearance):
        self.feature = feature.create(self, appearance)
        self._walkable = (self.is_open_door() or
                            _tile_is_walkable(appearance))

    def set_monster(self, appearance):
        """Sets self.monster and updates ohno.dungeon.curlevel.monsters"""
        new_monster = None
        if appearance is not None:
            new_monster = monster.create(self, appearance)

        if new_monster == self.monster:
            return

        if self.monster:
            self.level.monsters.remove(self.monster)

        if new_monster:
            self.level.monsters.append(new_monster)
            # Sometimes, a monster can open a door and walk onto the tile in
            # one turn, this will confuse ohno as it will still think it's a
            # door under the monster.
            if self.feature_isa('Door') and self.feature.closed:
                self.feature = None

        self.monster = new_monster

    def distance_from_hero(self):
        """
        Returns the distance from hero as calculated by ai.pathing.
        If the tile is unreachable, it will return float('inf').
        """
        assert self.ohno.ai.pathing.tick == self.ohno.tick
        return self.ohno.ai.pathing.dists[self.idx]

    # Methods for iterating neighbors
    @queryable
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
            for x2, y2 in ((dir[0] + x, dir[1] + y) for dir in dirs):
                if 0 <= x2 < 80 and 0 <= y2 < 21:
                    self._adjacent.append(self.level.tiles[y2 * 80 + x2])
            self._adjacent = tuple(self._adjacent)
        assert len(self._adjacent) <= 8
        return self._adjacent

    @queryable
    def orthogonal(self):
        if self._orthogonal is None:
            self._orthogonal = tuple(n for n in self.adjacent()
                                            if abs(self.idx - n.idx) in (1, 80))
        assert len(self._orthogonal) <= 4
        return self._orthogonal

    @queryable
    def vertical(self):
        if self._vertical is None:
            self._vertical = tuple(o for o in self.orthogonal()
                                            if abs(self.idx - o.idx) == 1)
        assert len(self._vertical) <= 2
        return self._vertical

    @queryable
    def horizontal(self):
        if self._horizontal is None:
            self._horizontal = tuple(o for o in self.orthogonal()
                                            if abs(self.idx - o.idx) == 80)
        assert len(self._horizontal) <= 2
        return self._horizontal

    # Methods to make it simpler to query
    def feature_isa(self, class_name):
        return self.feature_name == class_name

    def is_open_door(self):
        return (self.feature and
                self.feature.appearance.glyph in '-|' and
                self.feature.appearance.fg == 33)

    @property
    def is_wall(self):
        return (self.explored and self.feature and 
                self.feature.appearance.glyph in '|- ' and
                self.feature.appearance.fg == 37)

    @property
    def is_hallway(self):
        return (self.explored and self.feature and
                self.feature.appearance.glyph == '#' and
                self.feature.appearance.fg == 37)

    @property
    def is_floor(self):
        return (self.explored and self.feature and
                self.feature.appearance.glyph == '.' and
                self.feature.appearance.fg == 37)

    @property
    def has_monster(self):
        return self.monster is not None

    @property
    def has_closed_door(self):
        return self.feature_isa('Door') and self.feature.closed

    @property
    def feature_name(self):
        return self.feature.__class__.__name__ if self.feature else 'Unknown'

    @property
    def reachable(self):
        assert self.ohno.ai.pathing.is_uptodate()
        return self.distance_from_hero() != float('inf')

    @property
    def walkable(self):
        # This might be called before the tile is initialized, so make sure we
        # consider the case where appearance is None
        return (self.appearance and
                self._walkable and
                not self.monster and
                self.appearance.glyph != '0')
