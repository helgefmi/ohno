class BaseAction(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self._command = None

    def get_command(self):
        return self._command
