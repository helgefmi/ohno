from ohno.dungeon.level import Level

class Dungeon:
    def __init__(self, ohno):
        self.ohno = ohno
        self.levels = {}
        self.curlevel = None

    def update(self):
        dlvl = self.ohno.hero.dlvl
        if dlvl not in self.levels:
            self.ohno.logger.dungeon('Found new level (dlvl %d)!' % dlvl)
            self.levels[dlvl] = Level(self.ohno)
            self.curlevel = self.levels[dlvl]
        self.curlevel.update()
