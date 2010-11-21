class BaseStrategy(object):
    def __init__(self, ohno):
        self.ohno = ohno
    
    def get_action(self):
        raise NotImplementedError()
