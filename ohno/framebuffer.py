from ansiterm import Ansiterm

class FrameBuffer:
    def __init__(self, ohno):
        self.ohno = ohno
        self.ansiterm = Ansiterm(24, 80)

    def feed(self, data):
        return self.ansiterm.feed(data)

    def get_topline(self):
        return self.ansiterm.get_string(0, 79)

    def get_bottomlines(self):
        return self.ansiterm.get_string(80 * 22, 80 * 24)

    def get_maptiles(self):
        return self.ansiterm.get_tiles(80, 80 * 22)

    def get_cursor(self):
        cursor = self.ansiterm.get_cursor()
        return (int(cursor['x']), int(cursor['y']))
