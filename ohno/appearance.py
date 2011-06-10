class Appearance(object):
    """
    Represents the glyph, color and boldness of a tile on the framebuffer.
    This is an immutable class.
    """
    def __init__(self, glyph, color):
        self._glyph = glyph
        self._fg = color['fg']
        self._bold = color['bold']

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        ret = self.glyph
        ret += '%d' % (self.fg - 30)
        if self.bold:
            ret += 'b'
        return ret

    def __hash__(self):
        return hash(str(self))

    @property
    def glyph(self):
        return self._glyph

    @property
    def fg(self):
        return self._fg

    @property
    def bold(self):
        return self._bold

STAIRCASE_DOWN = Appearance('>', {'fg': 37, 'bold': False})
STAIRCASE_UP = Appearance('<', {'fg': 37, 'bold': False})
OPEN_DOOR = Appearance('-', {'fg': 33, 'bold': False})
FLOOR = Appearance('.', {'fg': 37, 'bold': False})
