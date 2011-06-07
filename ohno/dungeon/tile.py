import string

from ohno.dungeon.item.item import Item
from ohno.dungeon.monster.monster import Monster

from ohno.dungeon.feature import feature

from queryable import queryable

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

        self.feature = None
        self.items = []
        self.monster = None
        self.has_hero = None

        self._adjacent = None
        self._orthogonal = None
        self._horizontal = None
        self._vertical = None

    def set(self, appearance):
        """
        Will be called by `ohno.dungeon.level.update` if the current glyph or
        color has been changed since since the last update.
        `appearance` is "newly copied" (i.e. it's safe to change)
        """
        if _tile_is_feature(appearance):
            # Spaces ("dark part of the room") can never be set to explored
            # unless we have been adjacent to the square yet. This logic is
            # found in ohno.dungeon.level.
            self.explored = self.explored or appearance.glyph != ' '
            # If it's the first time we're seeing the feature of this tile or if
            # it has changed (i.e. water can spread to nearby floortiles).
            if (not self.feature) or self.feature.appearance != appearance:
                self.set_feature(appearance)
            self.items = []
            self.has_hero = False
            self.set_monster(None)
        elif _tile_is_item(appearance):
            self.ohno.logger.tile('Itemtile! %r' % self)
            self._walkable = True
            self.has_hero = False

            # If the appearance of the tile changes (i.e. something else
            # has dropped, or a monster picking up the topmost item),
            # we'll completely remove any previous examined items,
            # since the hero should reexamine the tile anyway.
            # If it stays the same, we'll simply assume nothing has changed.
            if not self.items or self.items[-1].appearance != appearance:
                self.ohno.logger.tile('New item!')
                self.items = [Item.create(self, appearance)]
                # Since this tile might have new information,
                # we set explored to False. That way, it'll be easier for our AI
                # to know this square is interesting.
                self.explored = False
            self.ohno.logger.tile('Itemtile is now %r' % self)
        elif self.idx == self.ohno.hero.get_position_idx():
            self.ohno.logger.tile('Herotile! %r' % self)
            assert not self.has_hero
            self._walkable = True
            self.has_hero = True
            self.set_monster(None)
            if self.ohno.hero.appearance != appearance:
                self.ohno.logger.tile('New hero! A was %s, now is %s' % (
                    self.ohno.hero.appearance, appearance
                ))
                # Not sure if we need this, but this seems like a good place to
                # check if we're polymorphed.
                self.ohno.hero.set_appearance(appearance)
            self.ohno.logger.tile('Herotile is now %r' % self)
        elif _tile_is_monster(appearance):
            # TODO: Might not be true if this is a stone giant standing on a
            #       boulder.
            self.ohno.logger.tile('Monstertile! %r' % self)
            self.has_hero = False
            self._walkable = True
            if (not self.monster) or self.monster.appearance != appearance:
                self.ohno.logger.tile('New monster!')
                self.set_monster(Monster.create(self, appearance))
            self.ohno.logger.tile('Monstertile is now %r' % self)

    def set_feature(self, appearance):
            self.feature = feature.create(self, appearance)
            self._walkable = (self.is_open_door() or
                                _tile_is_walkable(appearance))

    def set_monster(self, monster):
        """Sets self.monster and updates Levle.monsters"""
        if self.monster is not None:
            self.level.monsters.remove(self.monster)
        self.monster = monster
        self.level.monsters.append(monster)
    
    @property
    def appearance(self):
        """What does this tile look like right now?"""
        # This could be cached, but doing it like this works as a sanity check
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
    # TODO: Should perhaps use is_ prefix on every one of them
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
        return self.feature_is_a('Door') and self.feature.closed

    @property
    def feature_name(self):
        return self.feature.__class__.__name__ if self.feature else 'Unknown'

    @property
    def reachable(self):
        return self.distance_from_hero() != float('inf')

    @property
    def walkable(self):
        # TODO: The following is not true if we're currently a giant or have
        # the ability to fly (i think :)..
        # This might be called before the tile is initialized, so make sure we
        # consider the case where appearance is None
        return (self.appearance and
                self._walkable and
                self.appearance.glyph != '0')

    def feature_is_a(self, class_name):
        return self.feature_name == class_name

    def __str__(self):
        return '<Tile %d G=%s E=%d W=%d S=%d D=%f>' % (
            self.idx, self.appearance.glyph if self.appearance else ' ',
            self.explored, int(self.walkable or 0), self.searched,
            self.distance_from_hero() if self.ohno.ai.pathing.is_uptodate()
                                      else -1
        )

    def __repr__(self):
        return str(self)

    # TODO: Meh, move this to the pathing code.
    #       I see no other uses for this function.
    def is_open_door(self):
        return (self.feature and
                self.feature.appearance.glyph in '-|' and
                self.feature.appearance.fg == 33)

    # TODO: Meh, move this to the pathing code.
    #       I see no other uses for this function.
    def can_walk_diagonally(self):
        return not self.is_open_door()
