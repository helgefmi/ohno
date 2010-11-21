from ohno.ai.pathing import Pathing
from ohno.ai.strategy.strategy import Strategy

class AI(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.pathing = Pathing(ohno)
        self.strategy = Strategy(ohno)
