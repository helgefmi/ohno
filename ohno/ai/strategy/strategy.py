from itertools import chain
from ohno.ai.strategy.explore import Explore
from ohno.ai.strategy.battle import Battle

class Strategy(object):
    """The main AI controller"""
    def __init__(self, ohno):
        self.ohno = ohno
        self.strategies = [
            Battle(ohno),
            Explore(ohno), 
        ]

    def next_action(self):
        # TODO: This is just so I have something to play with. In the future,
        #       this might be coded into a bunch of if-else's with random
        #       spaghetti-code all over, that is, if I can't find something
        #       more elegant that I feel will be flexible enough to beat a game
        #       like nethack :-)
        self.ohno.logger.strategy('Getting the next action..')
        for strategy in self.strategies:
            action = strategy.get_action()
            if not action:
                continue
            self.ohno.logger.strategy('Got an action: %r' % action)
            return action
