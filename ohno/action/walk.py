from ohno import appearance
from ohno import util
from ohno.action.baseaction import BaseAction

class Walk(BaseAction):
    def __init__(self, ohno, tile):
        super(Walk, self).__init__(ohno)
        self.tile = tile
        self.next = None
        self._last_hero_tile = None
        self._last_delta = None

    def get_command(self):
        self.ohno.logger.action('[walk] Getting path to %r..' % self.tile)
        path = self.ohno.ai.pathing.get_path(self.tile)
        next = path.next()
        self.next = next
        delta = next.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[walk] next tile is %r (%d)' % (next, delta))
        assert abs(delta) in (1, 79, 80, 81)
        self._last_hero_tile = self.ohno.dungeon.curtile
        self._last_delta = delta
        return util.delta2vi(delta)

    def done(self, messages):
        if self._last_hero_tile != self.ohno.dungeon.curtile:
            return

        assert self.next.feature is None

        curtile_walls = set(self.ohno.dungeon.curtile.adjacent(is_wall=True))
        nexttile_walls = set(self.next.adjacent(is_wall=True))
        shared_walls = curtile_walls.intersection(nexttile_walls)

        # Moving diagonally through open doors is illegal.
        moved_diagonally = abs(self._last_delta) not in [1, 80]

        # If we're walking diagonally through an open door, we should always
        # share exactly one wall.
        shares_one_wall = len(shared_walls) == 1

        if moved_diagonally and shares_one_wall:
            self.ohno.logger.action(
                '[walk] Setting %s to open door.' % self.next
            )
            self.next.set_feature(appearance.OPEN_DOOR)
        elif self.next.appearance.glyph in '$*':
            self.ohno.logger.action(
                '[walk] Setting %s to not walkable.' % self.next
            )
            self.next._walkable = False
