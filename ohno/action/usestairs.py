from ohno.action.baseaction import BaseAction
from ohno import util

class UseStairs(BaseAction):
    def __init__(self, ohno, tile):
        super(UseStairs, self).__init__(ohno)
        self.tile = tile

    def get_command(self):
        self.ohno.logger.action('[usestairs] Getting command to walk up/down %r..' % self.tile)
        assert self.tile == self.ohno.dungeon.curtile
        return '>' if self.tile.feature.direction == 'down' else '<'
