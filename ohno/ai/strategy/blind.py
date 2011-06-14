from ohno.ai.strategy.basestrategy import BaseStrategy
from ohno.action.search import Search

class Blind(BaseStrategy):
    """
    Just to test hero.ohno; all strategies will be rewritten at some point.
    """
    def get_action(self):
        if not self.ohno.hero.blind:
            return

        return Search(self.ohno)
