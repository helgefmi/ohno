class BaseAction(object):
    def __init__(self, ohno):
        self.ohno = ohno

    def get_command(self):
        raise NotImplementedError()

    def done(self):
        pass
