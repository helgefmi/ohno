from ohno.action.baseaction import BaseAction
from ohno import util

class Open(BaseAction):
    def __init__(self, ohno, tile):
        super(Open, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[open] Getting command to open %r..' % self.tile)
        delta = self.tile.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[open] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return 'o' + util.delta2vi(delta)
