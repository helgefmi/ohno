from ohno.ai.pathing import Pathing
from ohno.ai.strategy.strategy import Strategy

class AI(object):
    """Class used for namespace purposes (ohno.ai.*)"""
    def __init__(self, ohno):
        self.ohno = ohno
        self.pathing = Pathing(ohno)
        self.strategy = Strategy(ohno)
