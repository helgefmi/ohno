import re

from queryable import queryable

from ohno.dungeon.tile import Tile
from ohno import appearance

class Level(object):
    inspectname = re.compile(
        '\('
            '(?P<peaceful>peaceful )?'
            '(?P<name>.*?)'
            '(?: - .*|, .*)?'
        '\)'
        '(?: \[seen: .*?\])?'
        '$'
    )

    def __init__(self, ohno, dlvl):
        self.ohno = ohno
        self.dlvl = dlvl
        # Tiles should only mutate, never be replaced by new ones.
        self.tiles = tuple(Tile(self, x) for x in xrange(21 * 80))
        self.monsters = []
        self.max_searched = 12

    def __str__(self):
        return '<Level %s>' % self.dlvl
    __repr__ = __str__

    def _farlook_monsters(self):
        # Check to see if there's a monster on this level that we're not sure
        # what is yet. 
        for monster in self.monsters:
            if not (len(monster.spoilers) > 1 or
                    (monster.peaceful is None and not monster.is_peaceful)):
                continue

            # No point in farlooking invisibles.
            if (monster.appearance == appearance.INVISIBLE_MONSTER or
               monster.appearance == appearance.MIMIC):
                continue

            self.ohno.logger.level('Doing farlook on %s (%s)' % (
                monster.tile, monster
            ))
            message = self.ohno.farlook(monster.tile)
            self.ohno.logger.level('Got message: %s' % message)
            info = Level.inspectname.search(message).groupdict()
            self.ohno.logger.level('Parsed: %s' % info)
            monster.monster_info(info)

    def update(self):
        """
        This will update the current level.
        1. Make changes to the tiles of this level.
        2. Update newly explored tiles as explored.
        3. Farlook interesting monsters.
        """
        self.ohno.logger.level('Updating level..')
        maptiles = self.ohno.framebuffer.get_maptiles()
        for i, tile in enumerate(self.tiles):
            maptile = maptiles[i]
            
            # No point in updating a tile that didn't change since last time.
            if tile.appearance != maptile:
                tile.set(maptile)

        self.ohno.dungeon.curtile.explored = True
        
        # Since empty spaces might both be walkable and not, the only way to
        # find out (well.. at this point anyway) is to stand adjacent to the
        # square and see if it lights up (see if the glyph changes or not).
        # If it doesn't, we need to set the tile to not walkable.
        if not self.ohno.hero.blind:
            for tile in self.ohno.dungeon.curtile.adjacent():
                if not tile.items:
                    tile.explored = True
                if tile.appearance.glyph == ' ':
                    tile._walkable = False

        self._farlook_monsters()

    def explored_progress(self):
        """
        How much of the level do we think is explored?
        Returns a percentage between where 100% is "I think I've
        explored everything".
        Used for deciding when to search instead of descending, but might be
        useful for other decisions (should I re-explore earlier levels if my
        ac is too low for the current level?)
        """
        # TODO: When we get better at branches, we might want to have different
        # algorithms for normal levels and mine levels.
        # TODO: Normal levels should count rooms as well as check the amount of
        # walkable tiles.
        num_walkable_tiles = len(
            list(self.tiles_where(walkable=True, explored=True))
        )

        # Let's try 300 as the value of explored walkable tiles a level has on
        # average.
        return (num_walkable_tiles / 300.) * 100

    @queryable
    def tiles_where(self):
        return self.tiles

    # events
    def on_message(self, event):
        curtile = self.ohno.dungeon.curtile

        if event.msgtype == 'locked_door':
            assert self.ohno.last_action.isa('Open')
            tile = self.ohno.last_action.tile
            assert tile.feature_isa('Door')
            self.ohno.logger.level('Locking %r@%s' % (tile, self))
            tile.feature.lock()

        if event.msgtype == 'found_staircase':
            if event.kwargs['direction'] == 'up':
                set_to = appearance.STAIRCASE_UP
            else:
                set_to = appearance.STAIRCASE_DOWN
            self.ohno.logger.level('Setting %s to %s' % (curtile, set_to))
            curtile.set_feature(set_to)

        if event.msgtype == 'found_open_door':
            self.ohno.logger.level('Setting %s to an open door' % curtile)
            curtile.set_feature(appearance.OPEN_DOOR)

        if event.msgtype == 'kicked_door':
            assert self.ohno.last_action.isa('Kick')
            tile = self.ohno.last_action.tile
            self.ohno.logger.level(
                'Setting %s to floor.' % self.ohno.last_action.tile
            )
            tile.set_feature(appearance.FLOOR)

        if event.msgtype == 'opened_door':
            assert self.ohno.last_action.isa('Open')
            self.ohno.logger.level(
                'Setting %s to floor.' % self.ohno.last_action.tile
            )
            self.ohno.last_action.tile.set_feature(appearance.OPEN_DOOR)

    def on_founditems(self, event):
        pass # TODO
