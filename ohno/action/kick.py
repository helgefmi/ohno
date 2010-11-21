from ohno.action.baseaction import BaseAction
from ohno import util

class Kick(BaseAction):
    def __init__(self, ohno, tile):
        super(Kick, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[kick] Getting command to kick %r..' % self.tile)
        delta = self.tile.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[kick] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return '\x04' + util.delta2vi(delta) # Ctrl-D
