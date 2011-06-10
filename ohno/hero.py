import re

def _parse_stat(stat):
    """'18/53' -> 15.53000"""
    stat = stat.replace('/', '.')
    if '**' in stat:
        return float(stat.replace('*', '0')) + 1
    return float(stat)

class Hero(object):
    # /usr/games/nethack
    # Helge the Skirmisher        St:16 Dx:10 Co:20 In:10 Wi:11 Ch:8  Lawful
    # Dlvl:2  $:32 HP:14(47) Pw:6(6) AC:10 Xp:4/134 T:1732
    # Helge the Wererat           St:16 Dx:10 Co:20 In:10 Wi:11 Ch:8
    # Lawful          Dlvl:2  $:32 HP:6(6) Pw:6(6) AC:6  HD:2 T:1564 Burdened
    # NAO
    # Ohnobot the Stripling       St:18/03 Dx:11 Co:18 In:8 Wi:9 Ch:8  Lawful
    # S:0     Dlvl:1  $:0  HP:18(18) Pw:1(1) AC:6  Xp:1/0 T:24

    parse_bottomline = re.compile("""
        (?P<name>\S+).*?\s+         # Name
        St:(?P<str>.+?)\s+          # Strength
        Dx:(?P<dex>.+?)\s+          # Dexterity
        Co:(?P<con>.+?)\s+          # Constitution
        In:(?P<int>.+?)\s+          # Intelligence
        Wi:(?P<wis>.+?)\s+          # Wisdom
        Ch:(?P<cha>.+?)\s+          # Charisma
        (?P<alignment>\w+)\s+       # Alginment
        (S:(?P<score>\d+)\s+)?      # Score (not in local client?)
        Dlvl:(?P<dlvl>\d+)\s+       # Dungeon level
        \$:(?P<gold>\d+)\s+         # Gold
        HP:(?P<hp>\d+)              # Current HP
        \((?P<maxhp>\d+)\)\s+       # Max HP
        Pw:(?P<pw>\d+)              # Current Power
        \((?P<maxpw>\d+)\)\s+       # Max Power
        AC:(?P<ac>\d+)\s+           # Armor Class
        ((HD:(?P<hd>\d+))|          # Monster level
        (Xp:(?P<level>\d+)/         # Level
        (?P<xp>\d+)))\s+            # Experience
        T:(?P<turns>\d+)            # Turns""",
        re.VERBOSE)

    def __init__(self, ohno):
        self.ohno = ohno

        self.appearance = None

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

        self.blind = False # TODO

    def __str__(self):
        return '<Hero ' + (' '.join('%s=%s' % (key, getattr(self, key))
                                        for key in self.__dict__) + '>')
    __repr__ = __str__

    def get_position_idx(self):
        return self.position[0] * 80 + self.position[1]

    def set_appearance(self, appearance):
        self.appearance = appearance

    def update(self):
        """
        Updates the hero attributes after we get new input from the framebuffer
        """
        self.ohno.logger.hero('Updating hero..')

        y, x = self.ohno.framebuffer.get_cursor()
        self.position = (y - 1, x) # Compensate for the topline

        bottomlines = self.ohno.framebuffer.get_bottomlines()
        match = Hero.parse_bottomline.match(bottomlines).groupdict()

        for key, value in match.iteritems():
            if key == 'level' and value is None:
                continue
            elif key == 'hd' and value is not None:
                key = 'level'
            elif key in ('str', 'dex', 'con', 'int', 'wis', 'cha'):
                value = _parse_stat(value)
            elif key in ('score', 'dlvl', 'gold', 'hp', 'maxhp', 'pw', 'maxpw',
                         'ac', 'level', 'xp', 'turns'):
                value = int(value or 0)
            setattr(self, key, value)

        self.ohno.logger.hero('Hero updated: %s' % self)
