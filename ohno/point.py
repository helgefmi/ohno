class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def idx(self):
        return self.x + 80 * self.y

    def set(self, x, y):
        self.x = x
        self.y = y

    def set_idx(self, idx):
        self.x = idx % 80
        self.y = idx / 80
