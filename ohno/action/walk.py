from ohno.action.baseaction import BaseAction
from ohno import util

class Walk(BaseAction):
    def __init__(self, ohno, tile):
        super(Walk, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[walk] Getting command to walk to %r..' % self.tile)
        path = self.ohno.ai.pathing.get_path(self.tile)
        next = path.next()
        self.ohno.logger.action('[walk] next tile is %r' % next)
        delta = next.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[walk] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return util.delta2vi(delta)
