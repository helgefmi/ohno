from ohno.ui.basemode import BaseMode

class NormalMode(BaseMode):
    """
    The default mode. Every other mode should be accessable through this mode.
    """
    def __init__(self, ohno):
        self.ohno = ohno
        self.ohno.paused = False

    def on_input(self, input):
        if input in '|sp':
            return super(NormalMode, self).on_input(input)
        elif input == 'd':
            from ohno.ui.debugmode import DebugMode
            return DebugMode

    def __str__(self):
        return 'normal'
