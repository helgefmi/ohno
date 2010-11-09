import re

def _parse_stat(stat):
    return float(stat.replace('/', '.'))

class Hero:
    parse_bottomline = re.compile('(\S+) .*?\s+St:(.+?) Dx:(.+?) Co:(.+?) In:(.+?) Wi:(.+?) Ch:(.+?)\s+(\w+)\s+S:(\d+)\s+Dlvl:(\d+)\s+\$:(\d+)\s+HP:(\d+)\((\d+)\)\s+Pw:(\d+)\((\d+)\) AC:(\d+)\s+Xp:(\d+)/(\d+)\s+T:(\d+)')
    def __init__(self, ohno):
        self.ohno = ohno

        self.position = (None, None)
        self.name = None
        self.str = self.dex = None
        self.con = self.int = None
        self.wis = self.cha = None
        self.alignment = None
        self.score = None
        self.dlvl = None
        self.gold = None
        self.hp = self.hpmax = None
        self.pw = self.pwmax = None
        self.ac = None
        self.level = self.xp = None
        self.turns = None

    def update(self):
        self.ohno.logger.hero('Updating hero..')

        self.position = self.ohno.framebuffer.get_cursor()

        bottomlines = self.ohno.framebuffer.get_bottomlines()
        match = Hero.parse_bottomline.match(bottomlines)
        assert match

        groups = match.groups()
        self.name = groups[0]
        self.str, self.dex, self.con, self.int, self.wis, self.cha = map(_parse_stat, groups[1:7])
        self.alignment = groups[7]
        self.score, self.dlvl, self.gold = map(int, groups[8:11])
        self.hp, self.hpmax, self.pw, self.pwmax = map(int, groups[11:15])
        self.ac, self.level, self.xp, self.turns = map(int, groups[15:])

        self.ohno.logger.hero('Hero updated: %s' % self)

    def __str__(self):
        return '<Hero %s str:%f dex:%f con:%f int:%f wis:%f cha:%f position:%d,%d alignment:%s score:%d dlvl:%d gold:%d hp:%d/%d pw:%d/%d ac:%d level:%d xp:%s turns:%d>' % (self.name, self.str, self.dex, self.con, self.int, self.wis, self.cha, self.position[0], self.position[1], self.alignment, self.score, self.dlvl, self.gold, self.hp, self.hpmax, self.pw, self.pwmax, self.ac, self.level, self.xp, self.turns)
