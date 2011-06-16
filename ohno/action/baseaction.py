class BaseAction(object):
    def __init__(self, ohno):
        self.ohno = ohno

    def get_command(self):
        raise NotImplementedError()

    def done(self, messages):
        pass

    def isa(self, name):
        return self.__class__.__name__ == name
