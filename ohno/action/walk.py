from ohno.action.baseaction import BaseAction
from ohno import util

class Walk(BaseAction):
    def __init__(self, ohno, to_tile):
        super(Walk, self).__init__(ohno)
        self.to_tile = to_tile

    def get_command(self):
        self.ohno.logger.action('[walk] Getting command to walk to %r..' % self.to_tile)
        path = self.ohno.ai.pathing.get_path(self.to_tile)
        next = path.next()
        self.ohno.logger.action('[walk] next tile is %r' % next)
        delta = next.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[walk] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return util.delta2vi(delta)
