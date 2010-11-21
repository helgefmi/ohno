from ohno.ai.strategy.basestrategy import BaseStrategy
from ohno.action.open import Open
from ohno.action.kick import Kick
from ohno.action.walk import Walk

# TODO: get_action should return a closed door or unexplored walkable tile
#       according to which is the closest instead of doing one first, then the
#       other.
class Explore(BaseStrategy):
    def _unexplored(self):
        tile = self.ohno.ai.pathing.search_where(explored=False, walkable=True).next()
        self.ohno.logger.strategy('[explore] Found unexplored at %r' % tile)
        return Walk(self.ohno, tile=tile)

    def _closed_doors(self):
        tile = self.ohno.ai.pathing.search_where(has_closed_door=True).next()
        assert tile.walkable == False

        self.ohno.logger.strategy('[explore] Found closed door at %r' % tile)
        if tile in self.ohno.dungeon.curtile.adjacent:
            if tile.feature.locked:
                self.ohno.logger.strategy('[explore] door is locked; kicking..')
                return Kick(self.ohno, tile=tile)
            else:
                self.ohno.logger.strategy('[explore] door is not locked; opening..')
                return Open(self.ohno, tile=tile)
        else:
            self.ohno.logger.strategy('[explore] door is not adjacent; walking..')
            return Walk(self.ohno, tile=tile)

    def get_action(self):
        for method in (self._unexplored, self._closed_doors):
            try:
                result = method()
                return result
            except StopIteration:
                self.ohno.logger.strategy('[explore] StopIteration at %r' % method)
