from ohno.action.baseaction import BaseAction
from ohno import util

class Melee(BaseAction):
    def __init__(self, ohno, tile):
        super(Melee, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[melee] Getting command to attack %r..' % self.tile)
        delta = self.tile.idx - self.ohno.dungeon.curtile.idx
        self.ohno.logger.action('[melee] .. and the delta is %d' % delta)
        assert abs(delta) in (1, 79, 80, 81)
        return util.delta2vi(delta)
