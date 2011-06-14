class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)
    __repr__ = __str__

    def idx(self):
        return self.x + 80 * self.y

    def set(self, x, y):
        self.x = x
        self.y = y

    def set_idx(self, idx):
        self.x = idx % 80
        self.y = idx / 80
