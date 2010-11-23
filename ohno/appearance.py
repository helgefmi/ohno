class Appearance(object):
    """
    Represents the glyph, color and boldness of a tile on the framebuffer.
    This is an immutable class.
    """
    def __init__(self, fbtile):
        self._glyph = fbtile.glyph
        self._fg = fbtile.color['fg']
        self._bold = fbtile.color['bold']

    glyph = property(lambda self:self._glyph)
    fg = property(lambda self:self._fg)
    bold = property(lambda self:self._bold)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        ret = self.glyph
        if self.fg != 37:
            ret += ',%d' % (self.fg - 30)
        if self.bold:
            ret += 'b'
        return ret

    def __hash__(self):
        return str(self).__hash__()