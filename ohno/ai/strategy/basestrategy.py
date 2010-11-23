class BaseStrategy(object):
    """Abstract class for strategies"""
    def __init__(self, ohno):
        self.ohno = ohno
    
    def get_action(self):
        raise NotImplementedError()
