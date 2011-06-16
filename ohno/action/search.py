from ohno.action.baseaction import BaseAction

class Search(BaseAction):
    def __init__(self, ohno, times=1):
        super(Search, self).__init__(ohno)
        # We're searching the squares adjacent to the tile we're standing on at
        # the point of pressing s, not the tile we're standing on the next turn
        # (we might get teleported for instance.)
        self.curtile = self.ohno.dungeon.curtile
        self.times = times

    def get_command(self):
        self.ohno.logger.action(
            '[search] Getting command to search %d times..' % self.times
        )
        return '%ds' % self.times

    def done(self, messages):
        """Update adjacent squares with the amount of searching we've done"""
        self.curtile.searched += self.times
        for neighbor in self.curtile.adjacent():
            # TODO: What if we get interrupted?
            neighbor.searched += self.times
