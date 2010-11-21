from ohno.ai.strategy.basestrategy import BaseStrategy
from ohno.action.walk import Walk

class Explore(BaseStrategy):
    def get_action(self):
        unexplored = self.ohno.ai.pathing.search_where(explored=False)
        try:
            first_unexplored = unexplored.next()
            self.ohno.logger.strategy('[explore] Found unexplored tile: %r' % first_unexplored)
            return Walk(self.ohno, to_tile=first_unexplored)
        except StopIteration:
            self.ohno.logger.strategy('[explore] No unexplored tiles found..')
