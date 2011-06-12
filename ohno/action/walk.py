from ohno import appearance
from ohno import util
from ohno.action.baseaction import BaseAction

class Walk(BaseAction):
    def __init__(self, ohno, tile):
        super(Walk, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[walk] Getting command to walk to %r..' % self.tile)
        path = self.ohno.ai.pathing.get_path(self.tile)
        next = path.next()
        self.next = next
        self.ohno.logger.action('[walk] next tile is %r' % next)
        delta = next.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[walk] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return util.delta2vi(delta)

    def done(self):
        # If we tried to move to a tile whose feature is hidden behind an item,
        # and was unsuccessful, it's probably an open door.
        success = self.next == self.ohno.dungeon.curtile
        if (not success and
           not self.next.feature and
           self.next.items and
           self.next in self.ohno.dungeon.curtile.adjacent()):
            if self.next.appearance.glyph == '$':
                self.ohno.logger.action('Setting %s to not walkable.' % self.next)
                self.next._walkable = False
            else:
                self.ohno.logger.action('Setting %s to open door.' % self.next)
                self.next.set_feature(appearance.OPEN_DOOR)
            return

        assert success, self.next
