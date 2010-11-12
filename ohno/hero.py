import re

def _parse_stat(stat):
    """'18/53' -> 15.53000"""
    return float(stat.replace('/', '.'))

class Hero:
    # /usr/games/nethack
    # Helge the Stripling         St:18/01 Dx:11 Co:16 In:9 Wi:11 Ch:11  Lawful       Dlvl:1  $:0  HP:18(18) Pw:1(1) AC:6  Exp:1
    # NAO
    # Ohnobot the Stripling       St:18/03 Dx:11 Co:18 In:8 Wi:9 Ch:8  Lawful S:0     Dlvl:1  $:0  HP:18(18) Pw:1(1) AC:6  Xp:1/0 T:24

    parse_bottomline = re.compile("""
        (?P<name>\S+).*?\s+         # Name
        St:(?P<str>.+?)\s+          # Strength
        Dx:(?P<dex>.+?)\s+          # Dexterity
        Co:(?P<con>.+?)\s+          # Constitution
        In:(?P<int>.+?)\s+          # Intelligence
        Wi:(?P<wis>.+?)\s+          # Wisdom
        Ch:(?P<cha>.+?)\s+          # Charisma
        (?P<alignment>\w+)\s+       # Alginment
        (S:(?P<score>\d+)\s+)?      # Score (optional)
        Dlvl:(?P<dlvl>\d+)\s+       # Dungeon level
        \$:(?P<gold>\d+)\s+         # Gold
        HP:(?P<hp>\d+)              # Current HP
        \((?P<maxhp>\d+)\)\s+       # Max HP
        Pw:(?P<pw>\d+)              # Current Power
        \((?P<maxpw>\d+)\)\s+       # Max Power
        AC:(?P<ac>\d+)\s+           # Armor Class
        (Xp:(?P<level1>\d+)/        # Level ?
        (?P<xp>\d+)|                # Experience
        Exp:(?P<level2>\d+))\s+     # Level ?
        (T:(?P<turns>\d+))?         # Turns (optional)""",
        re.VERBOSE)
    def __init__(self, ohno):
        self.ohno = ohno

        self.glyph = '@' # Don't do much with this one yet..

        self.position = (None, None)
        self.name = None
        self.str = self.dex = None
        self.con = self.int = None
        self.wis = self.cha = None
        self.alignment = None
        self.score = None
        self.dlvl = None
        self.gold = None
        self.hp = self.maxhp = None
        self.pw = self.maxpw = None
        self.ac = None
        self.level = self.xp = None
        self.turns = None

    def update(self):
        self.ohno.logger.hero('Updating hero..')

        y, x = self.ohno.framebuffer.get_cursor()
        self.position = (y - 1, x) # Compensate for the topline

        bottomlines = self.ohno.framebuffer.get_bottomlines()
        match = Hero.parse_bottomline.match(bottomlines).groupdict()

        for key, value in match.iteritems():
            if key.startswith('level'):
                if value is None:
                    continue
                key = 'level'

            if key in ('str', 'dex', 'con', 'int', 'wis', 'cha'):
                value = _parse_stat(value)
            elif key in ('score', 'dlvl', 'gold', 'hp', 'maxhp', 'pw', 'maxpw', 'ac', 'level', 'xp', 'turns'):
                value = int(value or 0)
            setattr(self, key, value)

        self.ohno.logger.hero('Hero updated: %s' % self)

    def get_position_idx(self):
        return self.position[0] * 80 + self.position[1]

    def __str__(self):
        return '<Hero %s str:%f dex:%f con:%f int:%f wis:%f cha:%f position:%d,%d alignment:%s score:%d dlvl:%d gold:%d hp:%d/%d pw:%d/%d ac:%d level:%d xp:%s turns:%d>' % (self.name, self.str, self.dex, self.con, self.int, self.wis, self.cha, self.position[0], self.position[1], self.alignment, self.score, self.dlvl, self.gold, self.hp, self.maxhp, self.pw, self.maxpw, self.ac, self.level, self.xp, self.turns)
