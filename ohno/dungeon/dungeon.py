from ohno.dungeon.level import Level
from ohno.event.message import MessageEvent

class Dungeon(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.levels = {}
        self.curlevel = None
        self.curtile = None

    def update(self):
        """
        1. Check if we're on a new level, and make on if we are
        2. Set self.curlevel and self.curtile, and update the current level
        """
        # TODO: Branches. We need to know which branch we are in and which
        #       levels are in which branch.
        #       This should probably be done inside this function, while
        #       the detection code should be in Level.
        dlvl = self.ohno.hero.dlvl
        if dlvl not in self.levels:
            self.ohno.logger.dungeon('Found new level (dlvl %d)!' % dlvl)
            self.levels[dlvl] = Level(self.ohno, dlvl)

        newlevel = self.levels[dlvl]
        if self.curlevel != newlevel:
            self.ohno.logger.dungeon(
                'We have moved from level %s to level %s' % (
                    self.curlevel,
                    newlevel
                )
            )
            if self.curlevel:
                MessageEvent.unsubscribe(self.curlevel.on_message)
            MessageEvent.subscribe(newlevel.on_message)
        self.curlevel = newlevel
        newlevel.update()

        idx = self.ohno.hero.get_position_idx()
        self.curtile = self.curlevel.tiles[idx]

        self.ohno.logger.dungeon('Current tile is %r' % self.curtile)

        # Some sanity checks
        assert self.curtile.idx == idx
        assert self.curtile.appearance == self.ohno.hero.appearance
        assert self.curtile.monster is None

        self.curlevel.farlook_monsters()
