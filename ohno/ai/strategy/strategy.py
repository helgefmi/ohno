from itertools import chain
from ohno.ai.strategy.explore import Explore
from ohno.ai.strategy.battle import Battle

class Strategy(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.strategies = [
            Battle(ohno),
            Explore(ohno), 
        ]

    def next_action(self):
        self.ohno.logger.strategy('Getting the next action..')
        for strategy in self.strategies:
            action = strategy.get_action()
            if not action:
                continue
            self.ohno.logger.strategy('Got an action: %r' % action)
            return action
