from ohno.appearance import Appearance
from collections import defaultdict
from queryable import queryable

# S_ {{{

S_ANT           = 1
S_BLOB          = 2
S_COCKATRICE    = 3
S_DOG           = 4
S_EYE           = 5
S_FELINE        = 6
S_GREMLIN       = 7
S_HUMANOID      = 8
S_IMP           = 9
S_JELLY         = 10
S_KOBOLD        = 11
S_LEPRECHAUN    = 12
S_MIMIC         = 13
S_NYMPH         = 14
S_ORC           = 15
S_PIERCER       = 16
S_QUADRUPED     = 17
S_RODENT        = 18
S_SPIDER        = 19
S_TRAPPER       = 20
S_UNICORN       = 21
S_VORTEX        = 22
S_WORM          = 23
S_XAN           = 24
S_LIGHT         = 25
S_ZRUTY         = 26
S_ANGEL         = 27
S_BAT           = 28
S_CENTAUR       = 29
S_DRAGON        = 30
S_ELEMENTAL     = 31
S_FUNGUS        = 32
S_GNOME         = 33
S_GIANT         = 34
S_JABBERWOCK    = 36
S_KOP           = 37
S_LICH          = 38
S_MUMMY         = 39
S_NAGA          = 40
S_OGRE          = 41
S_PUDDING       = 42
S_QUANTMECH     = 43
S_RUSTMONST     = 44
S_SNAKE         = 45
S_TROLL         = 46
S_UMBER         = 47
S_VAMPIRE       = 48
S_WRAITH        = 49
S_XORN          = 50
S_YETI          = 51
S_ZOMBIE        = 52
S_HUMAN         = 53
S_GHOST         = 54
S_GOLEM         = 55
S_DEMON         = 56
S_EEL           = 57
S_LIZARD        = 58
S_WORM_TAIL     = 59
S_MIMIC_DEF     = 60

# }}}
# G_ {{{

G_UNIQ      = 0x1000 # generated only once
G_NOHELL    = 0x0800 # not generated in "hell"
G_HELL      = 0x0400 # generated only in "hell"
G_NOGEN     = 0x0200 # generated only specially
G_SGROUP    = 0x0080 # appear in small groups normally
G_LGROUP    = 0x0040 # appear in large groups normally
G_GENO      = 0x0020 # can be genocided
G_NOCORPSE  = 0x0010 # no corpse left ever
G_FREQ      = 0x0007 # creation frequency mask
G_KNOWN     = 0x0004 # have been encountered
G_GENOD     = 0x0002 # have been genocided
G_EXTINCT   = 0x0001 # have been extinguished as
G_GONE      = (G_GENOD|G_EXTINCT)

# }}}
# AT_ {{{

AT_ANY = -1 # fake attack; dmgtype_fromattack wildcard
AT_NONE = 0 # passive monster (ex. acid blob)
AT_CLAW = 1 # claw (punch, hit, etc.)
AT_BITE = 2 # bite
AT_KICK = 3 # kick
AT_BUTT = 4 # head butt (ex. a unicorn)
AT_TUCH = 5 # touches
AT_STNG = 6 # sting
AT_HUGS = 7 # crushing bearhug
AT_SPIT = 10 # spits substance - ranged
AT_ENGL = 11 # engulf (swallow or by a cloud)
AT_BREA = 12 # breath - ranged
AT_EXPL = 13 # explodes - proximity
AT_BOOM = 14 # explodes when killed
AT_GAZE = 15 # gaze - ranged
AT_TENT = 16 # tentacles
AT_WEAP = 254 # uses weapon
AT_MAGC = 255 # uses magic spell(s)

# }}}
# AD_ {{{

AD_ANY = -1 # fake damage; attacktype_fordmg wildcard
AD_PHYS = 0 # ordinary physical
AD_MAGM = 1 # magic missiles
AD_FIRE = 2 # fire damage
AD_COLD = 3 # frost damage
AD_SLEE = 4 # sleep ray
AD_DISN = 5 # disintegration (death ray)
AD_ELEC = 6 # shock damage
AD_DRST = 7 # drains str (poison)
AD_ACID = 8 # acid damage
AD_SPC1 = 9 # for extension of buzz()
AD_SPC2 = 10 # for extension of buzz()
AD_BLND = 11 # blinds (yellow light)
AD_STUN = 12 # stuns
AD_SLOW = 13 # slows
AD_PLYS = 14 # paralyses
AD_DRLI = 15 # drains life levels (Vampire)
AD_DREN = 16 # drains magic energy
AD_LEGS = 17 # damages legs (xan)
AD_STON = 18 # petrifies (Medusa, cockatrice)
AD_STCK = 19 # sticks to you (mimic)
AD_SGLD = 20 # steals gold (leppie)
AD_SITM = 21 # steals item (nymphs)
AD_SEDU = 22 # seduces & steals multiple items
AD_TLPT = 23 # teleports you (Quantum Mech.)
AD_RUST = 24 # rusts armour (Rust Monster)*/
AD_CONF = 25 # confuses (Umber Hulk)
AD_DGST = 26 # digests opponent (trapper, etc.)
AD_HEAL = 27 # heals opponent's wounds (nurse)
AD_WRAP = 28 # special "stick" for eels
AD_WERE = 29 # confers lycanthropy
AD_DRDX = 30 # drains dexterity (quasit)
AD_DRCO = 31 # drains constitution
AD_DRIN = 32 # drains intelligence (mind flayer)
AD_DISE = 33 # confers diseases
AD_DCAY = 34 # decays organics (brown Pudding)
AD_SSEX = 35 # Succubus seduction (extended)
AD_HALU = 36 # causes hallucination
AD_DETH = 37 # for Death only
AD_PEST = 38 # for Pestilence only
AD_FAMN = 39 # for Famine only
AD_SLIM = 40 # turns you into green slime
AD_ENCH = 41 # remove enchantment (disenchanter)
AD_CORR = 42 # corrode armor (black pudding)
AD_CLRC = 240 # random clerical spell
AD_SPEL = 241 # random magic spell
AD_RBRE = 242 # random breath weapon
AD_SAMU = 252 # hits, may steal Amulet (Wizard)
AD_CURS = 253 # random curse (ex. gremlin)

# }}}
# MS_ {{{

MS_SILENT       = 0 # makes no sound
MS_BARK         = 1 # if full moon, may howl
MS_MEW          = 2 # mews or hisses
MS_ROAR         = 3 # roars
MS_GROWL        = 4 # growls
MS_SQEEK        = 5 # squeaks, as a rodent
MS_SQAWK        = 6 # squawks, as a bird
MS_HISS         = 7 # hisses
MS_BUZZ         = 8 # buzzes (killer bee)
MS_GRUNT        = 9 # grunts (or speaks own language)
MS_NEIGH        = 10 # neighs, as an equine
MS_WAIL         = 11 # wails, as a tortured soul
MS_GURGLE       = 12 # gurgles, as liquid or through saliva
MS_BURBLE       = 13 # burbles (jabberwock)
MS_ANIMAL       = 13 # up to here are animal noises
MS_SHRIEK       = 15 # wakes up others
MS_BONES        = 16 # rattles bones (skeleton)
MS_LAUGH        = 17 # grins, smiles, giggles, and laughs
MS_MUMBLE       = 18 # says something or other
MS_IMITATE      = 19 # imitates others (leocrotta)
MS_ORC          = MS_GRUNT # intelligent brutes
MS_HUMANOID     = 20 # generic traveling companion
MS_ARREST       = 21 # "Stop in the name of the law!" (Kops)
MS_SOLDIER      = 22 # army and watchmen expressions
MS_GUARD        = 23 # "Please drop that gold and follow me."
MS_DJINNI       = 24 # "Thank you for freeing me!"
MS_NURSE        = 25 # "Take off your shirt, please."
MS_SEDUCE       = 26 # "Hello, sailor." (Nymphs)
MS_VAMPIRE      = 27 # vampiric seduction, Vlad's exclamations
MS_BRIBE        = 28 # asks for money, or berates you
MS_CUSS         = 29 # berates (demons) or intimidates (Wiz)
MS_RIDER        = 30 # astral level special monsters
MS_LEADER       = 31 # your class leader
MS_NEMESIS      = 32 # your nemesis
MS_GUARDIAN     = 33 # your leader's guards
MS_SELL         = 34 # demand payment, complain about shoplifters
MS_ORACLE       = 35 # do a consultation
MS_PRIEST       = 36 # ask for contribution; do cleansing
MS_SPELL        = 37 # spellcaster not matching any of the above
MS_WERE         = 38 # lycanthrope in human form
MS_BOAST        = 39 # giants

# }}}
# MZ_ {{{

MZ_TINY     = 0 # < 2
MZ_SMALL    = 1 # 2-4
MZ_MEDIUM   = 2 # 4-7
MZ_HUMAN    = MZ_MEDIUM
MZ_LARGE    = 3 # 7-12
MZ_HUGE     = 4 # 12-25
MZ_GIGANTIC = 7 # off the scale

# }}}
# M1_ {{{

M1_FLY          = 0x00000001 # can fly or float
M1_SWIM         = 0x00000002 # can traverse water
M1_AMORPHOUS    = 0x00000004 # can flow under doors
M1_WALLWALK     = 0x00000008 # can phase thru rock
M1_CLING        = 0x00000010 # can cling to ceiling
M1_TUNNEL       = 0x00000020 # can tunnel thru rock
M1_NEEDPICK     = 0x00000040 # needs pick to tunnel
M1_CONCEAL      = 0x00000080 # hides under objects
M1_HIDE         = 0x00000100 # mimics, blends in with ceiling
M1_AMPHIBIOUS   = 0x00000200 # can survive underwater
M1_BREATHLESS   = 0x00000400 # doesn't need to breathe
M1_NOTAKE       = 0x00000800 # cannot pick up objects
M1_NOEYES       = 0x00001000 # no eyes to gaze into or blind
M1_NOHANDS      = 0x00002000 # no hands to handle things
M1_NOLIMBS      = 0x00006000 # no arms/legs to kick/wear on
M1_NOHEAD       = 0x00008000 # no head to behead
M1_MINDLESS     = 0x00010000 # has no mind--golem, zombie, mold
M1_HUMANOID     = 0x00020000 # has humanoid head/arms/torso
M1_ANIMAL       = 0x00040000 # has animal body
M1_SLITHY       = 0x00080000 # has serpent body
M1_UNSOLID      = 0x00100000 # has no solid or liquid body
M1_THICK_HIDE   = 0x00200000 # has thick hide or scales
M1_OVIPAROUS    = 0x00400000 # can lay eggs
M1_REGEN        = 0x00800000 # regenerates hit points
M1_SEE_INVIS    = 0x01000000 # can see invisible creatures
M1_TPORT        = 0x02000000 # can teleport
M1_TPORT_CNTRL  = 0x04000000 # controls where it teleports to
M1_ACID         = 0x08000000 # acidic to eat
M1_POIS         = 0x10000000 # poisonous to eat
M1_CARNIVORE    = 0x20000000 # eats corpses
M1_HERBIVORE    = 0x40000000 # eats fruits
M1_OMNIVORE     = 0x60000000 # eats both
M1_METALLIVORE  = 0x80000000 # eats metal
M1_METALLIVORE  = 0x80000000 # eats metal

# }}}
# M2_ {{{

M2_NOPOLY       = 0x00000001 # players mayn't poly into one
M2_UNDEAD       = 0x00000002 # is walking dead
M2_WERE         = 0x00000004 # is a lycanthrope
M2_HUMAN        = 0x00000008 # is a human
M2_ELF          = 0x00000010 # is an elf
M2_DWARF        = 0x00000020 # is a dwarf
M2_GNOME        = 0x00000040 # is a gnome
M2_ORC          = 0x00000080 # is an orc
M2_DEMON        = 0x00000100 # is a demon
M2_MERC         = 0x00000200 # is a guard or soldier
M2_LORD         = 0x00000400 # is a lord to its kind
M2_PRINCE       = 0x00000800 # is an overlord to its kind
M2_MINION       = 0x00001000 # is a minion of a deity
M2_GIANT        = 0x00002000 # is a giant
M2_MALE         = 0x00010000 # always male
M2_FEMALE       = 0x00020000 # always female
M2_NEUTER       = 0x00040000 # neither male nor female
M2_PNAME        = 0x00080000 # monster name is a proper name
M2_HOSTILE      = 0x00100000 # always starts hostile
M2_PEACEFUL     = 0x00200000 # always starts peaceful
M2_DOMESTIC     = 0x00400000 # can be tamed by feeding
M2_WANDER       = 0x00800000 # wanders randomly
M2_STALK        = 0x01000000 # follows you to other levels
M2_NASTY        = 0x02000000 # extra-nasty monster (more xp)
M2_STRONG       = 0x04000000 # strong (or big) monster
M2_ROCKTHROW    = 0x08000000 # throws boulders
M2_GREEDY       = 0x10000000 # likes gold
M2_JEWELS       = 0x20000000 # likes gems
M2_COLLECT      = 0x40000000 # picks up weapons and food
M2_MAGIC        = 0x80000000 # picks up magic items
M2_MAGIC        = 0x80000000 # picks up magic items

# }}}
# M3_ {{{

M3_WANTSAMUL    = 0x0001 # would like to steal the amulet
M3_WANTSBELL    = 0x0002 # wants the bell
M3_WANTSBOOK    = 0x0004 # wants the book
M3_WANTSCAND    = 0x0008 # wants the candelabrum
M3_WANTSARTI    = 0x0010 # wants the quest artifact
M3_WANTSALL     = 0x001f # wants any major artifact
M3_WAITFORU     = 0x0040 # waits to see you or get attacked
M3_CLOSE        = 0x0080 # lets you close unless attacked
M3_COVETOUS     = 0x001f # wants something
M3_WAITMASK     = 0x00c0 # waiting...
M3_INFRAVISION  = 0x0100 # has infravision
M3_INFRAVISIBLE = 0x0200 # visible by infravision

# }}}
# CLR_ {{{

CLR_BLACK           = 0
CLR_RED             = 1
CLR_GREEN           = 2
CLR_BROWN           = 3
CLR_BLUE            = 4
CLR_MAGENTA         = 5
CLR_CYAN            = 6
CLR_GRAY            = 7
CLR_ORANGE          = 9  # red
CLR_BRIGHT_GREEN    = 10 # green
CLR_YELLOW          = 11 # brown
CLR_BRIGHT_BLUE     = 12 # blue
CLR_BRIGHT_MAGENTA  = 13 # agenta
CLR_BRIGHT_CYAN     = 14 # cyan
CLR_WHITE           = 15 # gray

# }}}
# MR_ {{{

MR_FIRE     = 0x01 # resists fire
MR_COLD     = 0x02 # resists cold
MR_SLEEP    = 0x04 # resists sleep
MR_DISINT   = 0x08 # resists disintegration
MR_ELEC     = 0x10 # resists electricity
MR_POISON   = 0x20 # resists poison
MR_ACID     = 0x40 # resists acid
MR_STONE    = 0x80 # resists petrification

# }}}
# DEF_ {{{

DEF_ANT         = 'a'
DEF_BLOB        = 'b'
DEF_COCKATRICE  = 'c'
DEF_DOG         = 'd'
DEF_EYE         = 'e'
DEF_FELINE      = 'f'
DEF_GREMLIN     = 'g'
DEF_HUMANOID    = 'h'
DEF_IMP         = 'i'
DEF_JELLY       = 'j'
DEF_KOBOLD      = 'k'
DEF_LEPRECHAUN  = 'l'
DEF_MIMIC       = 'm'
DEF_NYMPH       = 'n'
DEF_ORC         = 'o'
DEF_PIERCER     = 'p'
DEF_QUADRUPED   = 'q'
DEF_RODENT      = 'r'
DEF_SPIDER      = 's'
DEF_TRAPPER     = 't'
DEF_UNICORN     = 'u'
DEF_VORTEX      = 'v'
DEF_WORM        = 'w'
DEF_XAN         = 'x'
DEF_LIGHT       = 'y'
DEF_ZRUTY       = 'z'
DEF_ANGEL       = 'A'
DEF_BAT         = 'B'
DEF_CENTAUR     = 'C'
DEF_DRAGON      = 'D'
DEF_ELEMENTAL   = 'E'
DEF_FUNGUS      = 'F'
DEF_GNOME       = 'G'
DEF_GIANT       = 'H'
DEF_JABBERWOCK  = 'J'
DEF_KOP         = 'K'
DEF_LICH        = 'L'
DEF_MUMMY       = 'M'
DEF_NAGA        = 'N'
DEF_OGRE        = 'O'
DEF_PUDDING     = 'P'
DEF_QUANTMECH   = 'Q'
DEF_RUSTMONST   = 'R'
DEF_SNAKE       = 'S'
DEF_TROLL       = 'T'
DEF_UMBER       = 'U'
DEF_VAMPIRE     = 'V'
DEF_WRAITH      = 'W'
DEF_XORN        = 'X'
DEF_YETI        = 'Y'
DEF_ZOMBIE      = 'Z'
DEF_HUMAN       = '@'
DEF_GHOST       = ' '
DEF_GOLEM       = '\''
DEF_DEMON       = '&'
DEF_EEL         = ';'
DEF_LIZARD      = ':'
DEF_INVISIBLE   = 'I'
DEF_WORM_TAIL   = '~'
DEF_MIMIC_DEF   = ']'

# }}}

# Monster {{{

class Monster(object):
    # glyphs {{{

    glyphs = (
        '\0',
        DEF_ANT,
        DEF_BLOB,
        DEF_COCKATRICE,
        DEF_DOG,
        DEF_EYE,
        DEF_FELINE,
        DEF_GREMLIN,
        DEF_HUMANOID,
        DEF_IMP,
        DEF_JELLY, # 10
        DEF_KOBOLD,
        DEF_LEPRECHAUN,
        DEF_MIMIC,
        DEF_NYMPH,
        DEF_ORC,
        DEF_PIERCER,
        DEF_QUADRUPED,
        DEF_RODENT,
        DEF_SPIDER,
        DEF_TRAPPER, # 20
        DEF_UNICORN,
        DEF_VORTEX,
        DEF_WORM,
        DEF_XAN,
        DEF_LIGHT,
        DEF_ZRUTY,
        DEF_ANGEL,
        DEF_BAT,
        DEF_CENTAUR,
        DEF_DRAGON, # 30
        DEF_ELEMENTAL,
        DEF_FUNGUS,
        DEF_GNOME,
        DEF_GIANT,
        '\0',
        DEF_JABBERWOCK,
        DEF_KOP,
        DEF_LICH,
        DEF_MUMMY,
        DEF_NAGA, # 40
        DEF_OGRE,
        DEF_PUDDING,
        DEF_QUANTMECH,
        DEF_RUSTMONST,
        DEF_SNAKE,
        DEF_TROLL,
        DEF_UMBER,
        DEF_VAMPIRE,
        DEF_WRAITH,
        DEF_XORN, # 50
        DEF_YETI,
        DEF_ZOMBIE,
        DEF_HUMAN,
        DEF_GHOST,
        DEF_GOLEM,
        DEF_DEMON,
        DEF_EEL,
        DEF_LIZARD,
        DEF_WORM_TAIL,
        DEF_MIMIC_DEF, # 60
    )

    # }}}
    def __init__(self, *args):
        args = list(args)
        self.name = args.pop(0) # full name
        self.mlet = args.pop(0) # symbol
        self.mlevel = args.pop(0) # base monster level
        self.mmove = args.pop(0) # move speed
        self.ac = args.pop(0) # (base) armor class
        self.mr = args.pop(0) # (base) magic resistance
        self.maligntyp = args.pop(0) # basic monster alignment
        self.geno = args.pop(0) # creation/geno mask value
        self.mattak = args.pop(0) # attacks matrix
        self.cwt = args.pop(0) # weight of corpse
        self.cnutrit = args.pop(0) # its nutritional value
        self.pxlth = args.pop(0) # length of extension
        self.msound = args.pop(0) # noise it makes
        self.msize = args.pop(0) # physical size
        self.mresists = args.pop(0) # resistances
        self.mconveys = args.pop(0) # conveyed by eating
        self.mflags1 = args.pop(0) # boolean bitflags
        self.mflags2 = args.pop(0) # more boolean bitflags
        self.mflags3 = args.pop(0) # yet more boolean bitflags
        self.mcolor = args.pop(0) # color to use

        self.appearance = Appearance(self.get_glyph(), {
            'fg': 30 + (self.mcolor % 8),
            'bold': self.mcolor > 8
        })

        assert args == []

    def debug(self):
        return '<Monster ' + (' '.join('%s=%s' % (key, getattr(self, key))
                                        for key in self.__dict__) + '>')

    def is_peaceful(self):
        return self.mflags2 & M2_PEACEFUL > 0

    def get_glyph(self):
        return Monster.glyphs[self.mlet]

    def __str__(self):
        return '<Monster "%s" A=%s P=%s L=%d>' % (
            self.name, self.appearance,
            int(self.is_peaceful()),
            self.mlevel
        )
    __repr__ = __str__

# }}}
# Attack {{{

class Attack(object):
    def __init__(self, aatyp, adtyp, damn, damd):
        # Some attacks can do no points of damage.  Additionally, some can
        # have special effects *and* do damage as well.  If damn and damd
        # are set, they may have a special meaning.  For example, if set
        # for a blinding attack, they determine the amount of time blinded.
        self.aatyp = aatyp # the gross attack type (eg. claw, bite, breath, ...)
        self.adtyp = adtyp # the damage type (eg. physical, fire, cold, spell, ...)
        self.damn = damn # the number of hit dice of damage from the attack.
        self.damd = damd # the number of sides on each die.

    def __str__(self):
        return '<Attack aatyp=%s adtyp=%s damn=%s damd=%s>' % (
            self.aatyp, self.adtyp, self.damn, self.damd
        )

    def __repr__(self):
        return str(self)

# }}}

# monsters {{{

monsters = (
Monster("giant ant", S_ANT, 2, 18, 3, 0, 0, (G_GENO|G_SGROUP|3), [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BROWN),
Monster("killer bee", S_ANT, 1, 18, -1, 0, 0, (G_GENO|G_LGROUP|2), [Attack(AT_STNG, AD_DRST, 1, 3), None, None, None, None, None], 1, 5, 0, MS_BUZZ, MZ_TINY, MR_POISON, MR_POISON, M1_ANIMAL|M1_FLY|M1_NOHANDS|M1_POIS, M2_HOSTILE|M2_FEMALE, 0, CLR_YELLOW),
Monster("soldier ant", S_ANT, 3, 18, 3, 0, 0, (G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 2, 4), Attack(AT_STNG, AD_DRST, 3, 4), None, None, None, None], 20, 5, 0, MS_SILENT, MZ_TINY, MR_POISON, MR_POISON, M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_POIS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BLUE),
Monster("fire ant", S_ANT, 3, 18, 3, 10, 0, (G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 2, 4), Attack(AT_BITE, AD_FIRE, 2, 4), None, None, None, None], 30, 10, 0, MS_SILENT, MZ_TINY, MR_FIRE, MR_FIRE, M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("giant beetle", S_ANT, 5, 6, 4, 0, 0, (G_GENO|3), [Attack(AT_BITE, AD_PHYS, 3, 6), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_LARGE, MR_POISON, MR_POISON, M1_ANIMAL|M1_NOHANDS|M1_POIS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BLACK),
Monster("queen bee", S_ANT, 9, 24, -4, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_STNG, AD_DRST, 1, 8), None, None, None, None, None], 1, 5, 0, MS_BUZZ, MZ_TINY, MR_POISON, MR_POISON, M1_ANIMAL|M1_FLY|M1_NOHANDS|M1_OVIPAROUS|M1_POIS, M2_HOSTILE|M2_FEMALE|M2_PRINCE, 0, CLR_MAGENTA),
Monster("acid blob", S_BLOB, 1, 3, 8, 0, 0, (G_GENO|2), [Attack(AT_NONE, AD_ACID, 1, 8), None, None, None, None, None], 30, 10, 0, MS_SILENT, MZ_TINY, MR_SLEEP|MR_POISON|MR_ACID|MR_STONE, MR_STONE, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_ACID, M2_WANDER|M2_NEUTER, 0, CLR_GREEN),
Monster("quivering blob", S_BLOB, 5, 1, 8, 0, 0, (G_GENO|2), [Attack(AT_TUCH, AD_PHYS, 1, 8), None, None, None, None, None], 200, 100, 0, MS_SILENT, MZ_SMALL, MR_SLEEP|MR_POISON, MR_POISON, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_WANDER|M2_HOSTILE|M2_NEUTER, 0, CLR_WHITE),
Monster("gelatinous cube", S_BLOB, 6, 6, 8, 0, 0, (G_GENO|2), [Attack(AT_TUCH, AD_PLYS, 2, 4), Attack(AT_NONE, AD_PLYS, 1, 4), None, None, None, None], 600, 150, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_ACID|MR_STONE, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_OMNIVORE|M1_ACID, M2_WANDER|M2_HOSTILE|M2_NEUTER, 0, CLR_CYAN),
Monster("chickatrice", S_COCKATRICE, 4, 4, 8, 30, 0, (G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 1, 2), Attack(AT_TUCH, AD_STON, 0, 0), Attack(AT_NONE, AD_STON, 0, 0), None, None, None], 10, 10, 0, MS_HISS, MZ_TINY, MR_POISON|MR_STONE, MR_POISON|MR_STONE, M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("cockatrice", S_COCKATRICE, 5, 6, 6, 30, 0, (G_GENO|5), [Attack(AT_BITE, AD_PHYS, 1, 3), Attack(AT_TUCH, AD_STON, 0, 0), Attack(AT_NONE, AD_STON, 0, 0), None, None, None], 30, 30, 0, MS_HISS, MZ_SMALL, MR_POISON|MR_STONE, MR_POISON|MR_STONE, M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE|M1_OVIPAROUS, M2_HOSTILE, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("pyrolisk", S_COCKATRICE, 6, 6, 6, 30, 0, (G_GENO|1), [Attack(AT_GAZE, AD_FIRE, 2, 6), None, None, None, None, None], 30, 30, 0, MS_HISS, MZ_SMALL, MR_POISON|MR_FIRE, MR_POISON|MR_FIRE, M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE|M1_OVIPAROUS, M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("jackal", S_DOG, 0, 12, 7, 0, 0, (G_GENO|G_SGROUP|3), [Attack(AT_BITE, AD_PHYS, 1, 2), None, None, None, None, None], 300, 250, 0, MS_BARK, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("fox", S_DOG, 0, 15, 7, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None, None], 300, 250, 0, MS_BARK, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("coyote", S_DOG, 1, 12, 7, 0, 0, (G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 300, 250, 0, MS_BARK, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("werejackal", S_DOG, 2, 12, 7, 10, -7, (G_NOGEN|G_NOCORPSE), [Attack(AT_BITE, AD_WERE, 1, 4), None, None, None, None, None], 300, 250, 0, MS_BARK, MZ_SMALL, MR_POISON, 0, M1_NOHANDS|M1_POIS|M1_REGEN|M1_CARNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("little dog", S_DOG, 2, 18, 6, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 150, 150, 0, MS_BARK, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("dog", S_DOG, 4, 16, 5, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1 ,6), None, None, None, None, None], 400, 200, 0, MS_BARK, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("large dog", S_DOG, 6, 15, 4, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 4), None, None, None, None, None], 800, 250, 0, MS_BARK, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_STRONG|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("dingo", S_DOG, 4, 16, 5, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1 ,6), None, None, None, None, None], 400, 200, 0, MS_BARK, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("wolf", S_DOG, 5, 12, 4, 0, 0, (G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 2, 4), None, None, None, None, None], 500, 250, 0, MS_BARK, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("werewolf", S_DOG, 5, 12, 4, 20, -7, (G_NOGEN|G_NOCORPSE), [Attack(AT_BITE, AD_WERE, 2, 6), None, None, None, None, None], 500, 250, 0, MS_BARK, MZ_MEDIUM, MR_POISON, 0, M1_NOHANDS|M1_POIS|M1_REGEN|M1_CARNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("warg", S_DOG, 7, 12, 4, 0, -5, (G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 850, 350, 0, MS_BARK, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("winter wolf cub", S_DOG, 5, 12, 4, 0, -5, (G_NOHELL|G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 1, 8), Attack(AT_BREA, AD_COLD, 1, 8), None, None, None, None], 250, 200, 0, MS_BARK, MZ_SMALL, MR_COLD, MR_COLD, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_CYAN),
Monster("winter wolf", S_DOG, 7, 12, 4, 20, 0, (G_NOHELL|G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 6), Attack(AT_BREA, AD_COLD, 2, 6), None, None, None, None], 700, 300, 0, MS_BARK, MZ_LARGE, MR_COLD, MR_COLD, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, 0, CLR_CYAN),
Monster("hell hound pup", S_DOG, 7, 12, 4, 20, -5, (G_HELL|G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 2, 6), Attack(AT_BREA, AD_FIRE, 2, 6), None, None, None, None], 200, 200, 0, MS_BARK, MZ_SMALL, MR_FIRE, MR_FIRE, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("hell hound", S_DOG, 12, 14, 2, 20, 0, (G_HELL|G_GENO|1), [Attack(AT_BITE, AD_PHYS, 3, 6), Attack(AT_BREA, AD_FIRE, 3, 6), None, None, None, None], 600, 300, 0, MS_BARK, MZ_MEDIUM, MR_FIRE, MR_FIRE, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_RED),
Monster("Cerberus", S_DOG, 12, 10, 2, 20, -7, (G_HELL|G_UNIQ|1), [Attack(AT_BITE, AD_PHYS, 3, 6), Attack(AT_BITE, AD_PHYS, 3, 6), Attack(AT_BITE, AD_PHYS, 3, 6), None, None, None], 1000, 350, 0, MS_BARK, MZ_LARGE, MR_FIRE, MR_FIRE, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_NOPOLY|M2_HOSTILE|M2_STRONG|M2_PNAME|M2_MALE, M3_INFRAVISIBLE, CLR_RED),
Monster("gas spore", S_EYE, 1, 3, 10, 0, 0, (G_NOCORPSE|G_GENO|1), [Attack(AT_BOOM, AD_PHYS, 4, 6), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_FLY|M1_BREATHLESS|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_HOSTILE|M2_NEUTER, 0, CLR_GRAY),
Monster("floating eye", S_EYE, 2, 1, 9, 10, 0, (G_GENO|5), [Attack(AT_NONE, AD_PLYS, 0,70), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_FLY|M1_AMPHIBIOUS|M1_NOLIMBS|M1_NOHEAD|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_BLUE),
Monster("freezing sphere", S_EYE, 6, 13, 4, 0, 0, (G_NOCORPSE|G_NOHELL|G_GENO|2), [Attack(AT_EXPL, AD_COLD, 4, 6), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_SMALL, MR_COLD, MR_COLD, M1_FLY|M1_BREATHLESS|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_WHITE),
Monster("flaming sphere", S_EYE, 6, 13, 4, 0, 0, (G_NOCORPSE|G_GENO|2), [Attack(AT_EXPL, AD_FIRE, 4, 6), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_SMALL, MR_FIRE, MR_FIRE, M1_FLY|M1_BREATHLESS|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_RED),
Monster("shocking sphere", S_EYE, 6, 13, 4, 0, 0, (G_NOCORPSE|G_GENO|2), [Attack(AT_EXPL, AD_ELEC, 4, 6), None, None, None, None, None], 10, 10, 0, MS_SILENT, MZ_SMALL, MR_ELEC, MR_ELEC, M1_FLY|M1_BREATHLESS|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_BRIGHT_BLUE),
Monster("kitten", S_FELINE, 2, 18, 6, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 150, 150, 0, MS_MEW, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_WANDER|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("housecat", S_FELINE, 4, 16, 5, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 200, 200, 0, MS_MEW, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("jaguar", S_FELINE, 4, 15, 6, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_BITE, AD_PHYS, 1, 8), None, None, None], 600, 300, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("lynx", S_FELINE, 5, 15, 6, 0, 0, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_BITE, AD_PHYS, 1, 10), None, None, None], 600, 300, 0, MS_GROWL, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE,M2_HOSTILE, M3_INFRAVISIBLE, CLR_CYAN),
Monster("panther", S_FELINE, 5, 15, 6, 0, 0, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_BITE, AD_PHYS, 1, 10), None, None, None], 600, 300, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE,M2_HOSTILE, M3_INFRAVISIBLE, CLR_BLACK),
Monster("large cat", S_FELINE, 6, 15, 4, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 4), None, None, None, None, None], 250, 250, 0, MS_MEW, MZ_SMALL, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_STRONG|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("tiger", S_FELINE, 6, 12, 6, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_BITE, AD_PHYS, 1,10), None, None, None], 600, 300, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("gremlin", S_GREMLIN, 5, 12, 2, 25, -9, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_BITE, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_CURS, 0, 0), None, None], 100, 20, 0, MS_LAUGH, MZ_SMALL, MR_POISON, MR_POISON, M1_SWIM|M1_HUMANOID|M1_POIS, M2_STALK, M3_INFRAVISIBLE, CLR_GREEN),
Monster("gargoyle", S_GREMLIN, 6, 10, -4, 0, -9, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_PHYS, 2, 6), Attack(AT_BITE, AD_PHYS, 2, 4), None, None, None], 1000, 200, 0, MS_GRUNT, MZ_HUMAN, MR_STONE, MR_STONE, M1_HUMANOID|M1_THICK_HIDE|M1_BREATHLESS, M2_HOSTILE|M2_STRONG, 0, CLR_BROWN),
Monster("winged gargoyle", S_GREMLIN, 9, 15, -2, 0, -12, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 3, 6), Attack(AT_CLAW, AD_PHYS, 3, 6), Attack(AT_BITE, AD_PHYS, 3, 4), None, None, None], 1200, 300, 0, MS_GRUNT, MZ_HUMAN, MR_STONE, MR_STONE, M1_FLY|M1_HUMANOID|M1_THICK_HIDE|M1_BREATHLESS|M1_OVIPAROUS, M2_LORD|M2_HOSTILE|M2_STRONG|M2_MAGIC, 0, CLR_MAGENTA),
Monster("hobbit", S_HUMANOID, 1, 9, 10, 0, 6, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 500, 200, 0, MS_HUMANOID, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GREEN),
Monster("dwarf", S_HUMANOID, 2, 6, 10, 10, 4, (G_GENO|3), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 900, 300, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_TUNNEL|M1_NEEDPICK|M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_DWARF|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("bugbear", S_HUMANOID, 3, 9, 5, 0, -6, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1250, 250, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("dwarf lord", S_HUMANOID, 4, 6, 10, 10, 5, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None], 900, 300, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_TUNNEL|M1_NEEDPICK|M1_HUMANOID|M1_OMNIVORE, M2_DWARF|M2_STRONG|M2_LORD|M2_MALE|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("dwarf king", S_HUMANOID, 6, 6, 10, 20, 6, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None], 900, 300, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_TUNNEL|M1_NEEDPICK|M1_HUMANOID|M1_OMNIVORE, M2_DWARF|M2_STRONG|M2_PRINCE|M2_MALE|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("mind flayer", S_HUMANOID, 9, 12, 5, 90, -8, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 4), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1), None, None], 1450, 400, 0, MS_HISS, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_FLY|M1_SEE_INVIS|M1_OMNIVORE, M2_HOSTILE|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("master mind flayer", S_HUMANOID, 13, 12, 0, 90, -8, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1), Attack(AT_TENT, AD_DRIN, 2, 1)], 1450, 400, 0, MS_HISS, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_FLY|M1_SEE_INVIS|M1_OMNIVORE, M2_HOSTILE|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("manes", S_IMP, 1, 3, 7, 0, -7, (G_GENO|G_LGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None], 100, 100, 0, MS_SILENT, MZ_SMALL, MR_SLEEP|MR_POISON, 0, M1_POIS, M2_HOSTILE|M2_STALK, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("homunculus", S_IMP, 2, 12, 6, 10, -7, (G_GENO|2), [Attack(AT_BITE, AD_SLEE, 1, 3), None, None, None, None, None], 60, 100, 0, MS_SILENT, MZ_TINY, MR_SLEEP|MR_POISON, MR_SLEEP|MR_POISON, M1_FLY|M1_POIS, M2_STALK, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GREEN),
Monster("imp", S_IMP, 3, 12, 2, 20, -7, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), None, None, None, None, None], 20, 10, 0, MS_CUSS, MZ_TINY, 0, 0, M1_REGEN, M2_WANDER|M2_STALK, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("lemure", S_IMP, 3, 3, 7, 0, -7, (G_HELL|G_GENO|G_LGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 3), None, None, None, None, None], 150, 100, 0, MS_SILENT, MZ_MEDIUM, MR_SLEEP|MR_POISON, MR_SLEEP, M1_POIS|M1_REGEN, M2_HOSTILE|M2_WANDER|M2_STALK|M2_NEUTER, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("quasit", S_IMP, 3, 15, 2, 20, -7, (G_GENO|2), [Attack(AT_CLAW, AD_DRDX, 1, 2), Attack(AT_CLAW, AD_DRDX, 1, 2), Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None], 200, 200, 0, MS_SILENT, MZ_SMALL, MR_POISON, MR_POISON, M1_REGEN, M2_STALK, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("tengu", S_IMP, 6, 13, 5, 30, 7, (G_GENO|3), [Attack(AT_BITE, AD_PHYS, 1, 7), None, None, None, None, None], 300, 200, 0, MS_SQAWK, MZ_SMALL, MR_POISON, MR_POISON, M1_TPORT|M1_TPORT_CNTRL, M2_STALK, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_CYAN),
Monster("blue jelly", S_JELLY, 4, 0, 8, 10, 0, (G_GENO|2), [Attack(AT_NONE, AD_COLD, 0, 6), None, None, None, None, None], 50, 20, 0, MS_SILENT, MZ_MEDIUM, MR_COLD|MR_POISON, MR_COLD|MR_POISON, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS |M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_BLUE),
Monster("spotted jelly", S_JELLY, 5, 0, 8, 10, 0, (G_GENO|1), [Attack(AT_NONE, AD_ACID, 0, 6), None, None, None, None, None], 50, 20, 0, MS_SILENT, MZ_MEDIUM, MR_ACID|MR_STONE, 0, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_ACID|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_GREEN),
Monster("ochre jelly", S_JELLY, 6, 3, 8, 20, 0, (G_GENO|2), [Attack(AT_ENGL, AD_ACID, 3, 6), Attack(AT_NONE, AD_ACID, 3, 6), None, None, None, None], 50, 20, 0, MS_SILENT, MZ_MEDIUM, MR_ACID|MR_STONE, 0, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_ACID|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("kobold", S_KOBOLD, 0, 6, 10, 0, -2, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 4), None, None, None, None, None], 400, 100, 0, MS_ORC, MZ_SMALL, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_OMNIVORE, M2_HOSTILE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("large kobold", S_KOBOLD, 1, 6, 10, 0, -3, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 450, 150, 0, MS_ORC, MZ_SMALL, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_OMNIVORE, M2_HOSTILE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("kobold lord", S_KOBOLD, 2, 6, 10, 0, -4, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 500, 200, 0, MS_ORC, MZ_SMALL, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_OMNIVORE, M2_HOSTILE|M2_LORD|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("kobold shaman", S_KOBOLD, 2, 6, 6, 10, -4, (G_GENO|1), [Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None, None], 450, 150, 0, MS_ORC, MZ_SMALL, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_OMNIVORE, M2_HOSTILE|M2_MAGIC, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BRIGHT_BLUE),
Monster("leprechaun", S_LEPRECHAUN, 5, 15, 8, 20, 0, (G_GENO|4), [Attack(AT_CLAW, AD_SGLD, 1, 2), None, None, None, None, None], 60, 30, 0, MS_LAUGH, MZ_TINY, 0, 0, M1_HUMANOID|M1_TPORT, M2_HOSTILE|M2_GREEDY, M3_INFRAVISIBLE, CLR_GREEN),
Monster("small mimic", S_MIMIC, 7, 3, 7, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 3, 4), None, None, None, None, None], 300, 200, 0, MS_SILENT, MZ_MEDIUM, MR_ACID, 0, M1_BREATHLESS|M1_AMORPHOUS|M1_HIDE|M1_ANIMAL|M1_NOEYES| M1_NOHEAD|M1_NOLIMBS|M1_THICK_HIDE|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BROWN),
Monster("large mimic", S_MIMIC, 8, 3, 7, 10, 0, (G_GENO|1), [Attack(AT_CLAW, AD_STCK, 3, 4), None, None, None, None, None], 600, 400, 0, MS_SILENT, MZ_LARGE, MR_ACID, 0, M1_CLING|M1_BREATHLESS|M1_AMORPHOUS|M1_HIDE|M1_ANIMAL|M1_NOEYES| M1_NOHEAD|M1_NOLIMBS|M1_THICK_HIDE|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, 0, CLR_RED),
Monster("giant mimic", S_MIMIC, 9, 3, 7, 20, 0, (G_GENO|1), [Attack(AT_CLAW, AD_STCK, 3, 6), Attack(AT_CLAW, AD_STCK, 3, 6), None, None, None, None], 800, 500, 0, MS_SILENT, MZ_LARGE, MR_ACID, 0, M1_CLING|M1_BREATHLESS|M1_AMORPHOUS|M1_HIDE|M1_ANIMAL|M1_NOEYES| M1_NOHEAD|M1_NOLIMBS|M1_THICK_HIDE|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, 0, CLR_MAGENTA),
Monster("wood nymph", S_NYMPH, 3, 12, 9, 20, 0, (G_GENO|2), [Attack(AT_CLAW, AD_SITM, 0, 0), Attack(AT_CLAW, AD_SEDU, 0, 0), None, None, None, None], 600, 300, 0, MS_SEDUCE, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_TPORT, M2_HOSTILE|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_GREEN),
Monster("water nymph", S_NYMPH, 3, 12, 9, 20, 0, (G_GENO|2), [Attack(AT_CLAW, AD_SITM, 0, 0), Attack(AT_CLAW, AD_SEDU, 0, 0), None, None, None, None], 600, 300, 0, MS_SEDUCE, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_TPORT|M1_SWIM, M2_HOSTILE|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_BLUE),
Monster("mountain nymph", S_NYMPH, 3, 12, 9, 20, 0, (G_GENO|2), [Attack(AT_CLAW, AD_SITM, 0, 0), Attack(AT_CLAW, AD_SEDU, 0, 0), None, None, None, None], 600, 300, 0, MS_SEDUCE, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_TPORT, M2_HOSTILE|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_BROWN),
Monster("goblin", S_ORC, 0, 6, 10, 0, -3, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 1, 4), None, None, None, None, None], 400, 100, 0, MS_ORC, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("hobgoblin", S_ORC, 1, 9, 10, 0, -4, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1000, 200, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("orc", S_ORC, 1, 9, 10, 0, -3, (G_GENO|G_NOGEN|G_LGROUP), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 850, 150, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("hill orc", S_ORC, 2, 9, 10, 0, -4, (G_GENO|G_LGROUP|2), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1000, 200, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_YELLOW),
Monster("Mordor orc", S_ORC, 3, 5, 10, 0, -5, (G_GENO|G_LGROUP|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1200, 200, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("Uruk-hai", S_ORC, 3, 7, 10, 0, -4, (G_GENO|G_LGROUP|1), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 1300, 300, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLACK),
Monster("orc shaman", S_ORC, 3, 9, 5, 10, -5, (G_GENO|1), [Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None, None], 1000, 300, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_MAGIC, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BRIGHT_BLUE),
Monster("orc-captain", S_ORC, 5, 5, 10, 0, -5, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None], 1350, 350, 0, MS_ORC, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_ORC|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("rock piercer", S_PIERCER, 3, 1, 3, 0, 0, (G_GENO|4), [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 200, 200, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_CLING|M1_HIDE|M1_ANIMAL|M1_NOEYES|M1_NOLIMBS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE, 0, CLR_GRAY),
Monster("iron piercer", S_PIERCER, 5, 1, 0, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 3, 6), None, None, None, None, None], 400, 300, 0, MS_SILENT, MZ_MEDIUM, 0, 0, M1_CLING|M1_HIDE|M1_ANIMAL|M1_NOEYES|M1_NOLIMBS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE, 0, CLR_CYAN),
Monster("glass piercer", S_PIERCER, 7, 1, 0, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 4, 6), None, None, None, None, None], 400, 300, 0, MS_SILENT, MZ_MEDIUM, MR_ACID, 0, M1_CLING|M1_HIDE|M1_ANIMAL|M1_NOEYES|M1_NOLIMBS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE, 0, CLR_WHITE),
Monster("rothe", S_QUADRUPED, 2, 9, 7, 0, 0, (G_GENO|G_SGROUP|4), [Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 1, 8), None, None, None], 400, 100, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("mumak", S_QUADRUPED, 5, 9, 0, 0, -2, (G_GENO|1), [Attack(AT_BUTT, AD_PHYS, 4,12), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None], 2500, 500, 0, MS_ROAR, MZ_LARGE, 0, 0, M1_ANIMAL|M1_THICK_HIDE|M1_NOHANDS|M1_HERBIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_GRAY),
Monster("leocrotta", S_QUADRUPED, 6, 18, 4, 10, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 2, 6), Attack(AT_BITE, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_PHYS, 2, 6), None, None, None], 1200, 500, 0, MS_IMITATE, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_RED),
Monster("wumpus", S_QUADRUPED, 8, 3, 2, 10, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 3, 6), None, None, None, None, None], 2500, 500, 0, MS_BURBLE, MZ_LARGE, 0, 0, M1_CLING|M1_ANIMAL|M1_NOHANDS|M1_OMNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_CYAN),
Monster("titanothere", S_QUADRUPED, 12, 12, 6, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 2, 8), None, None, None, None, None], 2650, 650, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_THICK_HIDE|M1_NOHANDS|M1_HERBIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_GRAY),
Monster("baluchitherium", S_QUADRUPED, 14, 12, 5, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 5, 4), Attack(AT_CLAW, AD_PHYS, 5, 4), None, None, None, None], 3800, 800, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_THICK_HIDE|M1_NOHANDS|M1_HERBIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_GRAY),
Monster("mastodon", S_QUADRUPED, 20, 12, 5, 0, 0, (G_GENO|1), [Attack(AT_BUTT, AD_PHYS, 4, 8), Attack(AT_BUTT, AD_PHYS, 4, 8), None, None, None, None], 3800, 800, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_THICK_HIDE|M1_NOHANDS|M1_HERBIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_BLACK),
Monster("sewer rat", S_RODENT, 0, 12, 7, 0, 0, (G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None, None], 20, 12, 0, MS_SQEEK, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("giant rat", S_RODENT, 1, 10, 7, 0, 0, (G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None, None], 30, 30, 0, MS_SQEEK, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("rabid rat", S_RODENT, 2, 12, 6, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DRCO, 2, 4), None, None, None, None, None], 30, 5, 0, MS_SQEEK, MZ_TINY, MR_POISON, 0, M1_ANIMAL|M1_NOHANDS|M1_POIS|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("wererat", S_RODENT, 2, 12, 6, 10, -7, (G_NOGEN|G_NOCORPSE), [Attack(AT_BITE, AD_WERE, 1, 4), None, None, None, None, None], 40, 30, 0, MS_SQEEK, MZ_TINY, MR_POISON, 0, M1_NOHANDS|M1_POIS|M1_REGEN|M1_CARNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("rock mole", S_RODENT, 3, 3, 0, 20, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 30, 30, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_TUNNEL|M1_ANIMAL|M1_NOHANDS|M1_METALLIVORE, M2_HOSTILE|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE, CLR_GRAY),
Monster("woodchuck", S_RODENT, 3, 3, 0, 20, 0, (G_NOGEN|G_GENO), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 30, 30, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_TUNNEL|M1_ANIMAL|M1_NOHANDS|M1_SWIM|M1_HERBIVORE, M2_WANDER|M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("cave spider", S_SPIDER, 1, 12, 3, 0, 0, (G_GENO|G_SGROUP|2), [Attack(AT_BITE, AD_PHYS, 1, 2), None, None, None, None, None], 50, 50, 0, MS_SILENT, MZ_TINY, MR_POISON, MR_POISON, M1_CONCEAL|M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_GRAY),
Monster("centipede", S_SPIDER, 2, 4, 3, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DRST, 1, 3), None, None, None, None, None], 50, 50, 0, MS_SILENT, MZ_TINY, MR_POISON, MR_POISON, M1_CONCEAL|M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_YELLOW),
Monster("giant spider", S_SPIDER, 5, 15, 4, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DRST, 2, 4), None, None, None, None, None], 100, 100, 0, MS_SILENT, MZ_LARGE, MR_POISON, MR_POISON, M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_POIS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, 0, CLR_MAGENTA),
Monster("scorpion", S_SPIDER, 5, 15, 3, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 1, 2), Attack(AT_CLAW, AD_PHYS, 1, 2), Attack(AT_STNG, AD_DRST, 1, 4), None, None, None], 50, 100, 0, MS_SILENT, MZ_SMALL, MR_POISON, MR_POISON, M1_CONCEAL|M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_POIS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_RED),
Monster("lurker above", S_TRAPPER, 10, 3, 3, 0, 0, (G_GENO|2), [Attack(AT_ENGL, AD_DGST, 1, 8), None, None, None, None, None], 800, 350, 0, MS_SILENT, MZ_HUGE, 0, 0, M1_HIDE|M1_FLY|M1_ANIMAL|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_CARNIVORE, M2_HOSTILE|M2_STALK|M2_STRONG, 0, CLR_GRAY),
Monster("trapper", S_TRAPPER, 12, 3, 3, 0, 0, (G_GENO|2), [Attack(AT_ENGL, AD_DGST, 1,10), None, None, None, None, None], 800, 350, 0, MS_SILENT, MZ_HUGE, 0, 0, M1_HIDE|M1_ANIMAL|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_CARNIVORE, M2_HOSTILE|M2_STALK|M2_STRONG, 0, CLR_GREEN),
Monster("white unicorn", S_UNICORN, 4, 24, 2, 70, 7, (G_GENO|2), [Attack(AT_BUTT, AD_PHYS, 1,12), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None, None], 1300, 300, 0, MS_NEIGH, MZ_LARGE, MR_POISON, MR_POISON, M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_JEWELS, M3_INFRAVISIBLE, CLR_WHITE),
Monster("gray unicorn", S_UNICORN, 4, 24, 2, 70, 0, (G_GENO|1), [Attack(AT_BUTT, AD_PHYS, 1,12), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None, None], 1300, 300, 0, MS_NEIGH, MZ_LARGE, MR_POISON, MR_POISON, M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_JEWELS, M3_INFRAVISIBLE, CLR_GRAY),
Monster("black unicorn", S_UNICORN, 4, 24, 2, 70, -7, (G_GENO|1), [Attack(AT_BUTT, AD_PHYS, 1,12), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None, None], 1300, 300, 0, MS_NEIGH, MZ_LARGE, MR_POISON, MR_POISON, M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_JEWELS, M3_INFRAVISIBLE, CLR_BLACK),
Monster("pony", S_UNICORN, 3, 16, 6, 0, 0, (G_GENO|2), [Attack(AT_KICK, AD_PHYS, 1, 6), Attack(AT_BITE, AD_PHYS, 1, 2), None, None, None, None], 1300, 250, 0, MS_NEIGH, MZ_MEDIUM, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_BROWN),
Monster("horse", S_UNICORN, 5, 20, 5, 0, 0, (G_GENO|2), [Attack(AT_KICK, AD_PHYS, 1, 8), Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None], 1500, 300, 0, MS_NEIGH, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_BROWN),
Monster("warhorse", S_UNICORN, 7, 24, 4, 0, 0, (G_GENO|2), [Attack(AT_KICK, AD_PHYS, 1, 10), Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None], 1800, 350, 0, MS_NEIGH, MZ_LARGE, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_HERBIVORE, M2_WANDER|M2_STRONG|M2_DOMESTIC, M3_INFRAVISIBLE, CLR_BROWN),
Monster("fog cloud", S_VORTEX, 3, 1, 0, 0, 0, (G_GENO|G_NOCORPSE|2), [Attack(AT_ENGL, AD_PHYS, 1, 6), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS| M1_AMORPHOUS|M1_UNSOLID, M2_HOSTILE|M2_NEUTER, 0, CLR_GRAY),
Monster("dust vortex", S_VORTEX, 4, 20, 2, 30, 0, (G_GENO|G_NOCORPSE|2), [Attack(AT_ENGL, AD_BLND, 2, 8), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("ice vortex", S_VORTEX, 5, 20, 2, 30, 0, (G_NOHELL|G_GENO|G_NOCORPSE|1), [Attack(AT_ENGL, AD_COLD, 1, 6), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_COLD|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_CYAN),
Monster("energy vortex", S_VORTEX, 6, 20, 2, 30, 0, (G_GENO|G_NOCORPSE|1), [Attack(AT_ENGL, AD_ELEC, 1, 6), Attack(AT_ENGL, AD_DREN, 0, 0), Attack(AT_NONE, AD_ELEC, 0, 4), None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_ELEC|MR_SLEEP|MR_DISINT|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS| M1_UNSOLID, M2_HOSTILE|M2_NEUTER, 0, CLR_BRIGHT_BLUE),
Monster("steam vortex", S_VORTEX, 7, 22, 2, 30, 0, (G_HELL|G_GENO|G_NOCORPSE|2), [Attack(AT_ENGL, AD_FIRE, 1, 8), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_FIRE|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS| M1_UNSOLID, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_BLUE),
Monster("fire vortex", S_VORTEX, 8, 22, 2, 30, 0, (G_HELL|G_GENO|G_NOCORPSE|1), [Attack(AT_ENGL, AD_FIRE, 1,10), Attack(AT_NONE, AD_FIRE, 0, 4), None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_FIRE|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS| M1_UNSOLID, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("baby long worm", S_WORM, 8, 3, 5, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 600, 250, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_SLITHY|M1_NOLIMBS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE, 0, CLR_BROWN),
Monster("baby purple worm", S_WORM, 8, 3, 5, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 600, 250, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_SLITHY|M1_NOLIMBS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_MAGENTA),
Monster("long worm", S_WORM, 8, 3, 5, 10, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 1500, 500, 0, MS_SILENT, MZ_GIGANTIC, 0, 0, M1_ANIMAL|M1_SLITHY|M1_NOLIMBS|M1_OVIPAROUS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE|M2_STRONG|M2_NASTY, 0, CLR_BROWN),
Monster("purple worm", S_WORM, 15, 9, 6, 20, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 2, 8), Attack(AT_ENGL, AD_DGST, 1,10), None, None, None, None], 2700, 700, 0, MS_SILENT, MZ_GIGANTIC, 0, 0, M1_ANIMAL|M1_SLITHY|M1_NOLIMBS|M1_OVIPAROUS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY, 0, CLR_MAGENTA),
Monster("grid bug", S_XAN, 0, 12, 9, 0, 0, (G_GENO|G_SGROUP|G_NOCORPSE|3), [Attack(AT_BITE, AD_ELEC, 1, 1), None, None, None, None, None], 15, 10, 0, MS_BUZZ, MZ_TINY, MR_ELEC|MR_POISON, 0, M1_ANIMAL, M2_HOSTILE, M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("xan", S_XAN, 7, 18, -4, 0, 0, (G_GENO|3), [Attack(AT_STNG, AD_LEGS, 1, 4), None, None, None, None, None], 300, 300, 0, MS_BUZZ, MZ_TINY, MR_POISON, MR_POISON, M1_FLY|M1_ANIMAL|M1_NOHANDS|M1_POIS, M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("yellow light", S_LIGHT, 3, 15, 0, 0, 0, (G_NOCORPSE|G_GENO|4), [Attack(AT_EXPL, AD_BLND, 10,20), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_SMALL, MR_FIRE|MR_COLD|MR_ELEC|MR_DISINT|MR_SLEEP|MR_POISON|MR_ACID| MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_UNSOLID|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("black light", S_LIGHT, 5, 15, 0, 0, 0, (G_NOCORPSE|G_GENO|2), [Attack(AT_EXPL, AD_HALU, 10,12), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_SMALL, MR_FIRE|MR_COLD|MR_ELEC|MR_DISINT|MR_SLEEP|MR_POISON|MR_ACID| MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_UNSOLID|M1_SEE_INVIS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_BLACK),
Monster("zruty", S_ZRUTY, 9, 8, 3, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_BITE, AD_PHYS, 3, 6), None, None, None], 1200, 600, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_BROWN),
Monster("couatl", S_ANGEL, 8, 10, 5, 30, 7, (G_NOHELL|G_SGROUP|G_NOCORPSE|1), [Attack(AT_BITE, AD_DRST, 2, 4), Attack(AT_BITE, AD_PHYS, 1, 3), Attack(AT_HUGS, AD_WRAP, 2, 4), None, None, None], 900, 400, 0, MS_HISS, MZ_LARGE, MR_POISON, 0, M1_FLY|M1_POIS, M2_MINION|M2_STALK|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GREEN),
Monster("Aleax", S_ANGEL, 10, 8, 0, 30, 7, (G_NOHELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_KICK, AD_PHYS, 1, 4), None, None, None], 1450, 400, 0, MS_IMITATE, MZ_HUMAN, MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_HUMANOID|M1_SEE_INVIS, M2_MINION|M2_STALK|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_YELLOW),
Monster("Angel", S_ANGEL, 14, 10, -4, 55, 12, (G_NOHELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_MAGC, AD_MAGM, 2, 6), None, None], 1450, 400, None, MS_CUSS, MZ_HUMAN, MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_FLY|M1_HUMANOID|M1_SEE_INVIS, M2_NOPOLY|M2_MINION|M2_STALK|M2_STRONG|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_WHITE),
Monster("ki-rin", S_ANGEL, 16, 18, -5, 90, 15, (G_NOHELL|G_NOCORPSE|1), [Attack(AT_KICK, AD_PHYS, 2, 4), Attack(AT_KICK, AD_PHYS, 2, 4), Attack(AT_BUTT, AD_PHYS, 3, 6), Attack(AT_MAGC, AD_SPEL, 2, 6), None, None], 1450, 400, 0, MS_NEIGH, MZ_LARGE, 0, 0, M1_FLY|M1_SEE_INVIS, M2_NOPOLY|M2_MINION|M2_STALK|M2_STRONG|M2_NASTY|M2_LORD, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_YELLOW),
Monster("Archon", S_ANGEL, 19, 16, -6, 80, 15, (G_NOHELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_GAZE, AD_BLND, 2, 6), Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_MAGC, AD_SPEL, 4, 6), None], 1450, 400, 0, MS_CUSS, MZ_LARGE, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_FLY|M1_HUMANOID|M1_SEE_INVIS|M1_REGEN, M2_NOPOLY|M2_MINION|M2_STALK|M2_STRONG|M2_NASTY|M2_LORD| M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("bat", S_BAT, 0, 22, 8, 0, 0, (G_GENO|G_SGROUP|1), [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 20, 20, 0, MS_SQEEK, MZ_TINY, 0, 0, M1_FLY|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_WANDER, M3_INFRAVISIBLE, CLR_BROWN),
Monster("giant bat", S_BAT, 2, 22, 7, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 30, 30, 0, MS_SQEEK, MZ_SMALL, 0, 0, M1_FLY|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_WANDER|M2_HOSTILE, M3_INFRAVISIBLE, CLR_RED),
Monster("raven", S_BAT, 4, 20, 6, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_BLND, 1, 6), None, None, None, None], 40, 20, 0, MS_SQAWK, MZ_SMALL, 0, 0, M1_FLY|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_WANDER|M2_HOSTILE, M3_INFRAVISIBLE, CLR_BLACK),
Monster("vampire bat", S_BAT, 5, 20, 6, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 1, 6), Attack(AT_BITE, AD_DRST, 0, 0), None, None, None, None], 30, 20, 0, MS_SQEEK, MZ_SMALL, MR_SLEEP|MR_POISON, 0, M1_FLY|M1_ANIMAL|M1_NOHANDS|M1_POIS|M1_REGEN|M1_OMNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BLACK),
Monster("plains centaur", S_CENTAUR, 4, 18, 4, 0, 0, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None, None], 2500, 500, 0, MS_HUMANOID, MZ_LARGE, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_STRONG|M2_GREEDY|M2_COLLECT, M3_INFRAVISIBLE, CLR_BROWN),
Monster("forest centaur", S_CENTAUR, 5, 18, 3, 10, -1, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None, None], 2550, 600, 0, MS_HUMANOID, MZ_LARGE, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_STRONG|M2_GREEDY|M2_COLLECT, M3_INFRAVISIBLE, CLR_GREEN),
Monster("mountain centaur", S_CENTAUR, 6, 20, 2, 10, -3, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1,10), Attack(AT_KICK, AD_PHYS, 1, 6), Attack(AT_KICK, AD_PHYS, 1, 6), None, None, None], 2550, 500, 0, MS_HUMANOID, MZ_LARGE, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_STRONG|M2_GREEDY|M2_COLLECT, M3_INFRAVISIBLE, CLR_CYAN),
Monster("baby gray dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, 0, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_GRAY),
Monster("baby silver dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, 0, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_BRIGHT_CYAN),
Monster("baby red dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_FIRE, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, M3_INFRAVISIBLE, CLR_RED),
Monster("baby white dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_COLD, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_WHITE),
Monster("baby orange dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_SLEEP, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_ORANGE),
Monster("baby black dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_DISINT, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_BLACK),
Monster("baby blue dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_ELEC, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_BLUE),
Monster("baby green dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_POISON, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE|M1_POIS, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_GREEN),
Monster("baby yellow dragon", S_DRAGON, 12, 9, 2, 10, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 1500, 500, 0, MS_ROAR, MZ_HUGE, MR_ACID|MR_STONE, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE|M1_ACID, M2_HOSTILE|M2_STRONG|M2_GREEDY|M2_JEWELS, 0, CLR_YELLOW),
Monster("gray dragon", S_DRAGON, 15, 9, -1, 20, 4, (G_GENO|1), [Attack(AT_BREA, AD_MAGM, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, 0, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_GRAY),
Monster("silver dragon", S_DRAGON, 15, 9, -1, 20, 4, (G_GENO|1), [Attack(AT_BREA, AD_COLD, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_COLD, 0, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_BRIGHT_CYAN),
Monster("red dragon", S_DRAGON, 15, 9, -1, 20, -4, (G_GENO|1), [Attack(AT_BREA, AD_FIRE, 6, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_FIRE, MR_FIRE, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, M3_INFRAVISIBLE, CLR_RED),
Monster("white dragon", S_DRAGON, 15, 9, -1, 20, -5, (G_GENO|1), [Attack(AT_BREA, AD_COLD, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_COLD, MR_COLD, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_WHITE),
Monster("orange dragon", S_DRAGON, 15, 9, -1, 20, 5, (G_GENO|1), [Attack(AT_BREA, AD_SLEE, 4,25), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_SLEEP, MR_SLEEP, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_ORANGE),
Monster("black dragon", S_DRAGON, 15, 9, -1, 20, -6, (G_GENO|1), [Attack(AT_BREA, AD_DISN, 4,10), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_DISINT, MR_DISINT, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_BLACK),
Monster("blue dragon", S_DRAGON, 15, 9, -1, 20, -7, (G_GENO|1), [Attack(AT_BREA, AD_ELEC, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_ELEC, MR_ELEC, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_BLUE),
Monster("green dragon", S_DRAGON, 15, 9, -1, 20, 6, (G_GENO|1), [Attack(AT_BREA, AD_DRST, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_POISON, MR_POISON, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE|M1_POIS, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_GREEN),
Monster("yellow dragon", S_DRAGON, 15, 9, -1, 20, 7, (G_GENO|1), [Attack(AT_BREA, AD_ACID, 4, 6), Attack(AT_BITE, AD_PHYS, 3, 8), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None], 4500, 1500, 0, MS_ROAR, MZ_GIGANTIC, MR_ACID|MR_STONE, MR_STONE, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_SEE_INVIS|M1_OVIPAROUS| M1_CARNIVORE|M1_ACID, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_GREEDY|M2_JEWELS|M2_MAGIC, 0, CLR_YELLOW),
Monster("stalker", S_ELEMENTAL, 8, 12, 3, 0, 0, (G_GENO|3), [Attack(AT_CLAW, AD_PHYS, 4, 4), None, None, None, None, None], 900, 400, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_FLY|M1_SEE_INVIS, M2_WANDER|M2_STALK|M2_HOSTILE|M2_STRONG, M3_INFRAVISION, CLR_WHITE),
Monster("air elemental", S_ELEMENTAL, 8, 36, 2, 30, 0, (G_NOCORPSE|1), [Attack(AT_ENGL, AD_PHYS, 1, 10), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_POISON|MR_STONE, 0, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_UNSOLID|M1_FLY, M2_STRONG|M2_NEUTER, 0, CLR_CYAN),
Monster("fire elemental", S_ELEMENTAL, 8, 12, 2, 30, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_FIRE, 3, 6), Attack(AT_NONE, AD_FIRE, 0, 4), None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUGE, MR_FIRE|MR_POISON|MR_STONE, 0, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_UNSOLID|M1_FLY|M1_NOTAKE, M2_STRONG|M2_NEUTER, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("earth elemental", S_ELEMENTAL, 8, 6, 2, 30, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 4, 6), None, None, None, None, None], 2500, 0, 0, MS_SILENT, MZ_HUGE, MR_FIRE|MR_COLD|MR_POISON|MR_STONE, 0, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_BREATHLESS| M1_WALLWALK|M1_THICK_HIDE, M2_STRONG|M2_NEUTER, 0, CLR_BROWN),
Monster("water elemental", S_ELEMENTAL, 8, 6, 2, 30, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 5, 6), None, None, None, None, None], 2500, 0, 0, MS_SILENT, MZ_HUGE, MR_POISON|MR_STONE, 0, M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_AMPHIBIOUS|M1_SWIM, M2_STRONG|M2_NEUTER, 0, CLR_BLUE),
Monster("lichen", S_FUNGUS, 0, 1, 9, 0, 0, (G_GENO|4), [Attack(AT_TUCH, AD_STCK, 0, 0), None, None, None, None, None], 20, 200, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_BRIGHT_GREEN),
Monster("brown mold", S_FUNGUS, 1, 0, 9, 0, 0, (G_GENO|1), [Attack(AT_NONE, AD_COLD, 0, 6), None, None, None, None, None], 50, 30, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_POISON, MR_COLD|MR_POISON, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("yellow mold", S_FUNGUS, 1, 0, 9, 0, 0, (G_GENO|2), [Attack(AT_NONE, AD_STUN, 0, 4), None, None, None, None, None], 50, 30, 0, MS_SILENT, MZ_SMALL, MR_POISON, MR_POISON, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_POIS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_YELLOW),
Monster("green mold", S_FUNGUS, 1, 0, 9, 0, 0, (G_GENO|1), [Attack(AT_NONE, AD_ACID, 0, 4), None, None, None, None, None], 50, 30, 0, MS_SILENT, MZ_SMALL, MR_ACID|MR_STONE, MR_STONE, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_ACID|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_GREEN),
Monster("red mold", S_FUNGUS, 1, 0, 9, 0, 0, (G_GENO|1), [Attack(AT_NONE, AD_FIRE, 0, 4), None, None, None, None, None], 50, 30, 0, MS_SILENT, MZ_SMALL, MR_FIRE|MR_POISON, MR_FIRE|MR_POISON, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, M3_INFRAVISIBLE, CLR_RED),
Monster("shrieker", S_FUNGUS, 3, 1, 7, 0, 0, (G_GENO|1), [None, None, None, None, None, None], 100, 100, 0, MS_SHRIEK, MZ_SMALL, MR_POISON, MR_POISON, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_MAGENTA),
Monster("violet fungus", S_FUNGUS, 3, 1, 7, 0, 0, (G_GENO|2), [Attack(AT_TUCH, AD_PHYS, 1, 4), Attack(AT_TUCH, AD_STCK, 0, 0), None, None, None, None], 100, 100, 0, MS_SILENT, MZ_SMALL, MR_POISON, MR_POISON, M1_BREATHLESS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD|M1_MINDLESS|M1_NOTAKE, M2_HOSTILE|M2_NEUTER, 0, CLR_MAGENTA),
Monster("gnome", S_GNOME, 1, 6, 10, 4, 0, (G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 650, 100, 0, MS_ORC, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_GNOME|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("gnome lord", S_GNOME, 3, 8, 10, 4, 0, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 700, 120, 0, MS_ORC, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_GNOME|M2_LORD|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("gnomish wizard", S_GNOME, 3, 10, 4, 10, 0, (G_GENO|1), [Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None, None], 700, 120, 0, MS_ORC, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_GNOME|M2_MAGIC, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BRIGHT_BLUE),
Monster("gnome king", S_GNOME, 5, 10, 10, 20, 0, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None, None], 750, 150, 0, MS_ORC, MZ_SMALL, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_GNOME|M2_PRINCE|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("giant", S_GIANT, 6, 6, 0, 0, 2, (G_GENO|G_NOGEN|1), [Attack(AT_WEAP, AD_PHYS, 2,10), None, None, None, None, None], 2250, 750, 0, MS_BOAST, MZ_HUGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("stone giant", S_GIANT, 6, 6, 0, 0, 2, (G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 2,10), None, None, None, None, None], 2250, 750, 0, MS_BOAST, MZ_HUGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("hill giant", S_GIANT, 8, 10, 6, 0, -2, (G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 2, 8), None, None, None, None, None], 2200, 700, 0, MS_BOAST, MZ_HUGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_CYAN),
Monster("fire giant", S_GIANT, 9, 12, 4, 5, 2, (G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 2,10), None, None, None, None, None], 2250, 750, 0, MS_BOAST, MZ_HUGE, MR_FIRE, MR_FIRE, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_YELLOW),
Monster("frost giant", S_GIANT, 10, 12, 3, 10, -3, (G_NOHELL|G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 2,12), None, None, None, None, None], 2250, 750, 0, MS_BOAST, MZ_HUGE, MR_COLD, MR_COLD, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_WHITE),
Monster("storm giant", S_GIANT, 16, 12, 3, 10, -3, (G_GENO|G_SGROUP|1), [Attack(AT_WEAP, AD_PHYS, 2, 12), None, None, None, None, None], 2250, 750, 0, MS_BOAST, MZ_HUGE, MR_ELEC, MR_ELEC, M1_HUMANOID|M1_CARNIVORE, M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_JEWELS, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("ettin", S_GIANT, 10, 12, 3, 0, 0, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 8), Attack(AT_WEAP, AD_PHYS, 3, 6), None, None, None, None], 1700, 500, 0, MS_GRUNT, MZ_HUGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("titan", S_GIANT, 16, 18, -3, 70, 9, (1), [Attack(AT_WEAP, AD_PHYS, 2, 8), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 2300, 900, 0, MS_SPELL, MZ_HUGE, 0, 0, M1_FLY|M1_HUMANOID|M1_OMNIVORE, M2_STRONG|M2_ROCKTHROW|M2_NASTY|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("minotaur", S_GIANT, 15, 15, 6, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_CLAW, AD_PHYS, 3,10), Attack(AT_CLAW, AD_PHYS, 3,10), Attack(AT_BUTT, AD_PHYS, 2, 8), None, None, None], 1500, 700, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("jabberwock", S_JABBERWOCK, 15, 12, -2, 50, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2,10), Attack(AT_BITE, AD_PHYS, 2,10), Attack(AT_CLAW, AD_PHYS, 2,10), Attack(AT_CLAW, AD_PHYS, 2,10), None, None], 1300, 600, 0, MS_BURBLE, MZ_LARGE, 0, 0, M1_ANIMAL|M1_FLY|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE, CLR_ORANGE),
Monster("Keystone Kop", S_KOP, 1, 6, 10, 10, 9, (G_GENO|G_LGROUP|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 1, 4), None, None, None, None, None], 1450, 200, 0, MS_ARREST, MZ_HUMAN, 0, 0, M1_HUMANOID, M2_HUMAN|M2_WANDER|M2_HOSTILE|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_BLUE),
Monster("Kop Sergeant", S_KOP, 2, 8, 10, 10, 10, (G_GENO|G_SGROUP|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 200, 0, MS_ARREST, MZ_HUMAN, 0, 0, M1_HUMANOID, M2_HUMAN|M2_WANDER|M2_HOSTILE|M2_STRONG|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_BLUE),
Monster("Kop Lieutenant", S_KOP, 3, 10, 10, 20, 11, (G_GENO|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 1450, 200, 0, MS_ARREST, MZ_HUMAN, 0, 0, M1_HUMANOID, M2_HUMAN|M2_WANDER|M2_HOSTILE|M2_STRONG|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_CYAN),
Monster("Kop Kaptain", S_KOP, 4, 12, 10, 20, 12, (G_GENO|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None, None], 1450, 200, 0, MS_ARREST, MZ_HUMAN, 0, 0, M1_HUMANOID, M2_HUMAN|M2_WANDER|M2_HOSTILE|M2_STRONG|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("lich", S_LICH, 11, 6, 0, 30, -9, (G_GENO|G_NOCORPSE|1), [Attack(AT_TUCH, AD_COLD, 1,10), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1200, 100, 0, MS_MUMBLE, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, MR_COLD, M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_HOSTILE|M2_MAGIC, M3_INFRAVISION, CLR_BROWN),
Monster("demilich", S_LICH, 14, 9, -2, 60, -12, (G_GENO|G_NOCORPSE|1), [Attack(AT_TUCH, AD_COLD, 3, 4), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1200, 100, 0, MS_MUMBLE, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, MR_COLD, M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_HOSTILE|M2_MAGIC, M3_INFRAVISION, CLR_RED),
Monster("master lich", S_LICH, 17, 9, -4, 90, -15, (G_HELL|G_GENO|G_NOCORPSE|1), [Attack(AT_TUCH, AD_COLD, 3, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1200, 100, 0, MS_MUMBLE, MZ_HUMAN, MR_FIRE|MR_COLD|MR_SLEEP|MR_POISON, MR_FIRE|MR_COLD, M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_HOSTILE|M2_MAGIC, M3_WANTSBOOK|M3_INFRAVISION, CLR_MAGENTA),
Monster("arch-lich", S_LICH, 25, 9, -6, 90, -15, (G_HELL|G_GENO|G_NOCORPSE|1), [Attack(AT_TUCH, AD_COLD, 5, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1200, 100, 0, MS_MUMBLE, MZ_HUMAN, MR_FIRE|MR_COLD|MR_SLEEP|MR_ELEC|MR_POISON, MR_FIRE|MR_COLD, M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_HOSTILE|M2_MAGIC, M3_WANTSBOOK|M3_INFRAVISION, CLR_MAGENTA),
Monster("kobold mummy", S_MUMMY, 3, 8, 6, 20, -2, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), None, None, None, None, None], 400, 50, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE, M3_INFRAVISION, CLR_BROWN),
Monster("gnome mummy", S_MUMMY, 4, 10, 6, 20, -3, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None, None], 650, 50, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_GNOME, M3_INFRAVISION, CLR_RED),
Monster("orc mummy", S_MUMMY, 5, 10, 5, 20, -4, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None, None], 850, 75, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_ORC|M2_GREEDY|M2_JEWELS, M3_INFRAVISION, CLR_GRAY),
Monster("dwarf mummy", S_MUMMY, 5, 10, 5, 20, -4, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None, None], 900, 150, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_DWARF|M2_GREEDY|M2_JEWELS, M3_INFRAVISION, CLR_RED),
Monster("elf mummy", S_MUMMY, 6, 12, 4, 30, -5, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 4), None, None, None, None, None], 800, 175, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_ELF, M3_INFRAVISION, CLR_GREEN),
Monster("human mummy", S_MUMMY, 6, 12, 4, 30, -5, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), None, None, None, None], 1450, 200, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE, M3_INFRAVISION, CLR_GRAY),
Monster("ettin mummy", S_MUMMY, 7, 12, 4, 30, -6, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_PHYS, 2, 6), None, None, None, None], 1700, 250, 0, MS_SILENT, MZ_HUGE, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_STRONG, M3_INFRAVISION, CLR_BLUE),
Monster("giant mummy", S_MUMMY, 8, 14, 3, 30, -7, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_CLAW, AD_PHYS, 3, 4), None, None, None, None], 2050, 375, 0, MS_SILENT, MZ_HUGE, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_HOSTILE|M2_GIANT|M2_STRONG|M2_JEWELS, M3_INFRAVISION, CLR_CYAN),
Monster("red naga hatchling", S_NAGA, 3, 10, 6, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 500, 100, 0, MS_MUMBLE, MZ_LARGE, MR_FIRE|MR_POISON, MR_FIRE|MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_NOTAKE|M1_OMNIVORE, M2_STRONG, M3_INFRAVISIBLE, CLR_RED),
Monster("black naga hatchling", S_NAGA, 3, 10, 6, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 500, 100, 0, MS_MUMBLE, MZ_LARGE, MR_POISON|MR_ACID|MR_STONE, MR_POISON|MR_STONE, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_ACID|M1_NOTAKE|M1_CARNIVORE, M2_STRONG, 0, CLR_BLACK),
Monster("golden naga hatchling", S_NAGA, 3, 10, 6, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 500, 100, 0, MS_MUMBLE, MZ_LARGE, MR_POISON, MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_NOTAKE|M1_OMNIVORE, M2_STRONG, 0, CLR_YELLOW),
Monster("guardian naga hatchling", S_NAGA, 3, 10, 6, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 500, 100, 0, MS_MUMBLE, MZ_LARGE, MR_POISON, MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_NOTAKE|M1_OMNIVORE, M2_STRONG, 0, CLR_GREEN),
Monster("red naga", S_NAGA, 6, 12, 4, 0, -4, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 4), Attack(AT_BREA, AD_FIRE, 2, 6), None, None, None, None], 2600, 400, 0, MS_MUMBLE, MZ_HUGE, MR_FIRE|MR_POISON, MR_FIRE|MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_OVIPAROUS|M1_NOTAKE|M1_OMNIVORE, M2_STRONG, M3_INFRAVISIBLE, CLR_RED),
Monster("black naga", S_NAGA, 8, 14, 2, 10, 4, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 6), Attack(AT_SPIT, AD_ACID, 0, 0), None, None, None, None], 2600, 400, 0, MS_MUMBLE, MZ_HUGE, MR_POISON|MR_ACID|MR_STONE, MR_POISON|MR_STONE, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_OVIPAROUS|M1_ACID|M1_NOTAKE| M1_CARNIVORE, M2_STRONG, 0, CLR_BLACK),
Monster("golden naga", S_NAGA, 10, 14, 2, 70, 5, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 2, 6), Attack(AT_MAGC, AD_SPEL, 4, 6), None, None, None, None], 2600, 400, 0, MS_MUMBLE, MZ_HUGE, MR_POISON, MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_OVIPAROUS|M1_NOTAKE|M1_OMNIVORE, M2_STRONG, 0, CLR_YELLOW),
Monster("guardian naga", S_NAGA, 12, 16, 0, 50, 7, (G_GENO|1), [Attack(AT_BITE, AD_PLYS, 1, 6), Attack(AT_SPIT, AD_DRST, 1, 6), Attack(AT_HUGS, AD_PHYS, 2, 4), None, None, None], 2600, 400, 0, MS_MUMBLE, MZ_HUGE, MR_POISON, MR_POISON, M1_NOLIMBS|M1_SLITHY|M1_THICK_HIDE|M1_OVIPAROUS|M1_POIS|M1_NOTAKE| M1_OMNIVORE, M2_STRONG, 0, CLR_GREEN),
Monster("ogre", S_OGRE, 5, 10, 5, 0, -3, (G_SGROUP|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 5), None, None, None, None, None], 1600, 500, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("ogre lord", S_OGRE, 7, 12, 3, 30, -5, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None, None], 1700, 700, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_STRONG|M2_LORD|M2_MALE|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("ogre king", S_OGRE, 9, 14, 4, 60, -7, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 3, 5), None, None, None, None, None], 1700, 750, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_CARNIVORE, M2_STRONG|M2_PRINCE|M2_MALE|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("gray ooze", S_PUDDING, 3, 1, 8, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_RUST, 2, 8), None, None, None, None, None], 500, 250, 0, MS_SILENT, MZ_MEDIUM, MR_FIRE|MR_COLD|MR_POISON|MR_ACID|MR_STONE, MR_FIRE|MR_COLD|MR_POISON, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_OMNIVORE|M1_ACID, M2_HOSTILE|M2_NEUTER, 0, CLR_GRAY),
Monster("brown pudding", S_PUDDING, 5, 3, 8, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DCAY, 0, 0), None, None, None, None, None], 500, 250, 0, MS_SILENT, MZ_MEDIUM, MR_COLD|MR_ELEC|MR_POISON|MR_ACID|MR_STONE, MR_COLD|MR_ELEC|MR_POISON, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_OMNIVORE|M1_ACID, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("black pudding", S_PUDDING, 10, 6, 6, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_CORR, 3, 8), Attack(AT_NONE, AD_CORR, 0, 0), None, None, None, None], 900, 250, 0, MS_SILENT, MZ_LARGE, MR_COLD|MR_ELEC|MR_POISON|MR_ACID|MR_STONE, MR_COLD|MR_ELEC|MR_POISON, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_OMNIVORE|M1_ACID, M2_HOSTILE|M2_NEUTER, 0, CLR_BLACK),
Monster("green slime", S_PUDDING, 6, 6, 6, 0, 0, (G_HELL|G_GENO|1), [Attack(AT_TUCH, AD_SLIM, 1, 4), Attack(AT_NONE, AD_SLIM, 0, 0), None, None, None, None], 400, 150, 0, MS_SILENT, MZ_LARGE, MR_COLD|MR_ELEC|MR_POISON|MR_ACID|MR_STONE, 0, M1_BREATHLESS|M1_AMORPHOUS|M1_NOEYES|M1_NOLIMBS|M1_NOHEAD| M1_MINDLESS|M1_OMNIVORE|M1_ACID|M1_POIS, M2_HOSTILE|M2_NEUTER, 0, CLR_GREEN),
Monster("quantum mechanic", S_QUANTMECH, 7, 12, 3, 10, 0, (G_GENO|3), [Attack(AT_CLAW, AD_TLPT, 1, 4), None, None, None, None, None], 1450, 20, 0, MS_HUMANOID, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE|M1_POIS|M1_TPORT, M2_HOSTILE, M3_INFRAVISIBLE, CLR_CYAN),
Monster("rust monster", S_RUSTMONST, 5, 18, 2, 0, 0, (G_GENO|2), [Attack(AT_TUCH, AD_RUST, 0, 0), Attack(AT_TUCH, AD_RUST, 0, 0), Attack(AT_NONE, AD_RUST, 0, 0), None, None, None], 1000, 250, 0, MS_SILENT, MZ_MEDIUM, 0, 0, M1_SWIM|M1_ANIMAL|M1_NOHANDS|M1_METALLIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BROWN),
Monster("disenchanter", S_RUSTMONST, 12, 12, -10, 0, -3, (G_HELL|G_GENO|2), [Attack(AT_CLAW, AD_ENCH, 4, 4), Attack(AT_NONE, AD_ENCH, 0, 0), None, None, None, None], 750, 200, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_CARNIVORE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BLUE),
Monster("garter snake", S_SNAKE, 1, 8, 8, 0, 0, (G_LGROUP|G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 2), None, None, None, None, None], 50, 60, 0, MS_HISS, MZ_TINY, 0, 0, M1_SWIM|M1_CONCEAL|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY|M1_OVIPAROUS| M1_CARNIVORE|M1_NOTAKE, 0, 0, CLR_GREEN),
Monster("snake", S_SNAKE, 4, 15, 3, 0, 0, (G_GENO|2), [Attack(AT_BITE, AD_DRST, 1, 6), None, None, None, None, None], 100, 80, 0, MS_HISS, MZ_SMALL, MR_POISON, MR_POISON, M1_SWIM|M1_CONCEAL|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY|M1_POIS| M1_OVIPAROUS|M1_CARNIVORE|M1_NOTAKE, M2_HOSTILE, 0, CLR_BROWN),
Monster("water moccasin", S_SNAKE, 4, 15, 3, 0, 0, (G_GENO|G_NOGEN|G_LGROUP), [Attack(AT_BITE, AD_DRST, 1, 6), None, None, None, None, None], 150, 80, 0, MS_HISS, MZ_SMALL, MR_POISON, MR_POISON, M1_SWIM|M1_CONCEAL|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY|M1_POIS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, 0, CLR_RED),
Monster("pit viper", S_SNAKE, 6, 15, 2, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DRST, 1, 4), Attack(AT_BITE, AD_DRST, 1, 4), None, None, None, None], 100, 60, 0, MS_HISS, MZ_MEDIUM, MR_POISON, MR_POISON, M1_SWIM|M1_CONCEAL|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY|M1_POIS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, M3_INFRAVISION, CLR_BLUE),
Monster("python", S_SNAKE, 6, 3, 5, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 1, 4), Attack(AT_TUCH, AD_PHYS, 0, 0), Attack(AT_HUGS, AD_WRAP, 1, 4), Attack(AT_HUGS, AD_PHYS, 2, 4), None, None], 250, 100, 0, MS_HISS, MZ_LARGE, 0, 0, M1_SWIM|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE|M2_STRONG, M3_INFRAVISION, CLR_MAGENTA),
Monster("cobra", S_SNAKE, 6, 18, 2, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_DRST, 2, 4), Attack(AT_SPIT, AD_BLND, 0, 0), None, None, None, None], 250, 100, 0, MS_HISS, MZ_MEDIUM, MR_POISON, MR_POISON, M1_SWIM|M1_CONCEAL|M1_NOLIMBS|M1_ANIMAL|M1_SLITHY|M1_POIS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, 0, CLR_BLUE),
Monster("troll", S_TROLL, 7, 12, 4, 0, -3, (G_GENO|2), [Attack(AT_WEAP, AD_PHYS, 4, 2), Attack(AT_CLAW, AD_PHYS, 4, 2), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None], 800, 350, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_REGEN|M1_CARNIVORE, M2_STRONG|M2_STALK|M2_HOSTILE, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("ice troll", S_TROLL, 9, 10, 2, 20, -3, (G_NOHELL|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_COLD, 2, 6), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None], 1000, 300, 0, MS_GRUNT, MZ_LARGE, MR_COLD, MR_COLD, M1_HUMANOID|M1_REGEN|M1_CARNIVORE, M2_STRONG|M2_STALK|M2_HOSTILE, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_WHITE),
Monster("rock troll", S_TROLL, 9, 12, 0, 0, -3, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 3, 6), Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None], 1200, 300, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_REGEN|M1_CARNIVORE, M2_STRONG|M2_STALK|M2_HOSTILE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_CYAN),
Monster("water troll", S_TROLL, 11, 14, 4, 40, -3, (G_NOGEN|G_GENO), [Attack(AT_WEAP, AD_PHYS, 2, 8), Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None], 1200, 350, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_REGEN|M1_CARNIVORE|M1_SWIM, M2_STRONG|M2_STALK|M2_HOSTILE, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("Olog-hai", S_TROLL, 13, 12, -4, 0, -7, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 3, 6), Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None], 1500, 400, 0, MS_GRUNT, MZ_LARGE, 0, 0, M1_HUMANOID|M1_REGEN|M1_CARNIVORE, M2_STRONG|M2_STALK|M2_HOSTILE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("umber hulk", S_UMBER, 9, 6, 2, 25, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_BITE, AD_PHYS, 2, 5), Attack(AT_GAZE, AD_CONF, 0, 0), None, None], 1200, 500, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_TUNNEL|M1_CARNIVORE, M2_STRONG, M3_INFRAVISIBLE, CLR_BROWN),
Monster("vampire", S_VAMPIRE, 10, 12, 1, 25, -8, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_BITE, AD_DRLI, 1, 6), None, None, None, None], 1450, 400, 0, MS_VAMPIRE, MZ_HUMAN, MR_SLEEP|MR_POISON, 0, M1_FLY|M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE, CLR_RED),
Monster("vampire lord", S_VAMPIRE, 12, 14, 0, 50, -9, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_BITE, AD_DRLI, 1, 8), None, None, None, None], 1450, 400, 0, MS_VAMPIRE, MZ_HUMAN, MR_SLEEP|MR_POISON, 0, M1_FLY|M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_LORD|M2_MALE, M3_INFRAVISIBLE, CLR_BLUE),
Monster("Vlad the Impaler", S_VAMPIRE, 14, 18, -3, 80, -10, (G_NOGEN|G_NOCORPSE|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 10), Attack(AT_BITE, AD_DRLI, 1, 10), None, None, None, None], 1450, 400, 0, MS_VAMPIRE, MZ_HUMAN, MR_SLEEP|MR_POISON, 0, M1_FLY|M1_BREATHLESS|M1_HUMANOID|M1_POIS|M1_REGEN, M2_NOPOLY|M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_PNAME|M2_STRONG| M2_NASTY|M2_PRINCE|M2_MALE, M3_WAITFORU|M3_WANTSCAND|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("barrow wight", S_WRAITH, 3, 12, 5, 5, -3, (G_GENO|G_NOCORPSE|1), [Attack(AT_WEAP, AD_DRLI, 0, 0), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_PHYS, 1, 4), None, None, None], 1200, 0, 0, MS_SPELL, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_HUMANOID, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_COLLECT, 0, CLR_GRAY),
Monster("wraith", S_WRAITH, 6, 12, 4, 15, -6, (G_GENO|2), [Attack(AT_TUCH, AD_DRLI, 1, 6), None, None, None, None, None], 0, 0, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_BREATHLESS|M1_FLY|M1_HUMANOID|M1_UNSOLID, M2_UNDEAD|M2_STALK|M2_HOSTILE, 0, CLR_BLACK),
Monster("Nazgul", S_WRAITH, 13, 12, 0, 25, -17, (G_GENO|G_NOCORPSE|1), [Attack(AT_WEAP, AD_DRLI, 1, 4), Attack(AT_BREA, AD_SLEE, 2,25), None, None, None, None], 1450, 0, 0, MS_SPELL, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_HUMANOID, M2_NOPOLY|M2_UNDEAD|M2_STALK|M2_STRONG|M2_HOSTILE|M2_MALE|M2_COLLECT, 0, CLR_MAGENTA),
Monster("xorn", S_XORN, 8, 9,-2, 20, 0, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 4, 6), None, None], 1200, 700, 0, MS_ROAR, MZ_MEDIUM, MR_FIRE|MR_COLD|MR_STONE, MR_STONE, M1_BREATHLESS|M1_WALLWALK|M1_THICK_HIDE|M1_METALLIVORE, M2_HOSTILE|M2_STRONG, 0, CLR_BROWN),
Monster("monkey", S_YETI, 2, 12, 6, 0, 0, (G_GENO|1), [Attack(AT_CLAW, AD_SITM, 0, 0), Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None], 100, 50, 0, MS_GROWL, MZ_SMALL, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, 0, M3_INFRAVISIBLE, CLR_GRAY),
Monster("ape", S_YETI, 4, 12, 6, 0, 0, (G_GENO|G_SGROUP|2), [Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None], 1100, 500, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_STRONG, M3_INFRAVISIBLE, CLR_BROWN),
Monster("owlbear", S_YETI, 5, 12, 5, 0, 0, (G_GENO|3), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_HUGS, AD_PHYS, 2, 8), None, None, None], 1700, 700, 0, MS_ROAR, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE, CLR_BROWN),
Monster("yeti", S_YETI, 5, 15, 6, 0, 0, (G_GENO|2), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None], 1600, 700, 0, MS_GROWL, MZ_LARGE, MR_COLD, MR_COLD, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_WHITE),
Monster("carnivorous ape", S_YETI, 6, 12, 6, 0, 0, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_HUGS, AD_PHYS, 1, 8), None, None, None], 1250, 550, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_CARNIVORE, M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_BLACK),
Monster("sasquatch", S_YETI, 7, 15, 6, 0, 2, (G_GENO|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_KICK, AD_PHYS, 1, 8), None, None, None], 1550, 750, 0, MS_GROWL, MZ_LARGE, 0, 0, M1_ANIMAL|M1_HUMANOID|M1_SEE_INVIS|M1_OMNIVORE, M2_STRONG, M3_INFRAVISIBLE, CLR_GRAY),
Monster("kobold zombie", S_ZOMBIE, 0, 6, 10, 0, -2, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), None, None, None, None, None], 400, 50, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_STALK|M2_HOSTILE, M3_INFRAVISION, CLR_BROWN),
Monster("gnome zombie", S_ZOMBIE, 1, 6, 10, 0, -2, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 5), None, None, None, None, None], 650, 50, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_GNOME, M3_INFRAVISION, CLR_BROWN),
Monster("orc zombie", S_ZOMBIE, 2, 6, 9, 0, -3, (G_GENO|G_SGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None, None], 850, 75, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_ORC, M3_INFRAVISION, CLR_GRAY),
Monster("dwarf zombie", S_ZOMBIE, 2, 6, 9, 0, -3, (G_GENO|G_SGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None, None], 900, 150, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_DWARF, M3_INFRAVISION, CLR_RED),
Monster("elf zombie", S_ZOMBIE, 3, 6, 9, 0, -3, (G_GENO|G_SGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 7), None, None, None, None, None], 800, 175, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_ELF, M3_INFRAVISION, CLR_GREEN),
Monster("human zombie", S_ZOMBIE, 4, 6, 8, 0, -3, (G_GENO|G_SGROUP|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 8), None, None, None, None, None], 1450, 200, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_UNDEAD|M2_STALK|M2_HOSTILE, M3_INFRAVISION, CLR_WHITE),
Monster("ettin zombie", S_ZOMBIE, 6, 8, 6, 0, -4, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1,10), Attack(AT_CLAW, AD_PHYS, 1,10), None, None, None, None], 1700, 250, 0, MS_SILENT, MZ_HUGE, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_STRONG, M3_INFRAVISION, CLR_BLUE),
Monster("giant zombie", S_ZOMBIE, 8, 8, 6, 0, -4, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_CLAW, AD_PHYS, 2, 8), None, None, None, None], 2050, 375, 0, MS_SILENT, MZ_HUGE, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_UNDEAD|M2_STALK|M2_HOSTILE|M2_GIANT|M2_STRONG, M3_INFRAVISION, CLR_CYAN),
Monster("ghoul", S_ZOMBIE, 3, 6, 10, 0, -2, (G_GENO|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PLYS, 1, 2), Attack(AT_CLAW, AD_PHYS, 1, 3), None, None, None, None], 400, 50, 0, MS_SILENT, MZ_SMALL, MR_COLD|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_POIS, M2_UNDEAD|M2_WANDER|M2_HOSTILE, M3_INFRAVISION, CLR_BLACK),
Monster("skeleton", S_ZOMBIE, 12, 8, 4, 0, 0, (G_NOCORPSE|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_TUCH, AD_SLOW, 1, 6), None, None, None, None], 300, 5, 0, MS_BONES, MZ_HUMAN, MR_COLD|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_UNDEAD|M2_WANDER|M2_HOSTILE|M2_STRONG|M2_COLLECT|M2_NASTY, M3_INFRAVISION, CLR_WHITE),
Monster("straw golem", S_GOLEM, 3, 12, 10, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 2), Attack(AT_CLAW, AD_PHYS, 1, 2), None, None, None, None], 400, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_HOSTILE|M2_NEUTER, 0, CLR_YELLOW),
Monster("paper golem", S_GOLEM, 3, 12, 10, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 3), None, None, None, None, None], 400, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_HOSTILE|M2_NEUTER, 0, CLR_WHITE),
Monster("rope golem", S_GOLEM, 4, 9, 8, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_HUGS, AD_PHYS, 6, 1), None, None, None], 450, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("gold golem", S_GOLEM, 5, 9, 6, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 3), Attack(AT_CLAW, AD_PHYS, 2, 3), None, None, None, None], 450, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON|MR_ACID, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_HOSTILE|M2_NEUTER, 0, CLR_YELLOW),
Monster("leather golem", S_GOLEM, 6, 6, 6, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_PHYS, 1, 6), None, None, None, None], 800, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("wood golem", S_GOLEM, 7, 3, 4, 0, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 3, 4), None, None, None, None, None], 900, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_HOSTILE|M2_NEUTER, 0, CLR_BROWN),
Monster("flesh golem", S_GOLEM, 9, 8, 9, 30, 0, (1), [Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_CLAW, AD_PHYS, 2, 8), None, None, None, None], 1400, 600, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID, M2_HOSTILE|M2_STRONG, 0, CLR_RED),
Monster("clay golem", S_GOLEM, 11, 7, 7, 40, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 3,10), None, None, None, None, None], 1550, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_HOSTILE|M2_STRONG, 0, CLR_BROWN),
Monster("stone golem", S_GOLEM, 14, 6, 5, 50, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 3, 8), None, None, None, None, None], 1900, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON|MR_STONE, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_HOSTILE|M2_STRONG, 0, CLR_GRAY),
Monster("glass golem", S_GOLEM, 16, 6, 1, 50, 0, (G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 2, 8), Attack(AT_CLAW, AD_PHYS, 2, 8), None, None, None, None], 1800, 0, 0, MS_SILENT, MZ_LARGE, MR_SLEEP|MR_POISON|MR_ACID, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE, M2_HOSTILE|M2_STRONG, 0, CLR_CYAN),
Monster("iron golem", S_GOLEM, 18, 6, 3, 60, 0, (G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 4,10), Attack(AT_BREA, AD_DRST, 4, 6), None, None, None, None], 2000, 0, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_BREATHLESS|M1_MINDLESS|M1_HUMANOID|M1_THICK_HIDE|M1_POIS, M2_HOSTILE|M2_STRONG|M2_COLLECT, 0, CLR_CYAN),
Monster("human", S_HUMAN, 0, 12, 10, 0, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("wererat", S_HUMAN, 2, 12, 10, 10, -7, (1), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_WERE, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_REGEN|M1_OMNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE|M2_HUMAN|M2_COLLECT, M3_INFRAVISIBLE, CLR_BROWN),
Monster("werejackal", S_HUMAN, 2, 12, 10, 10, -7, (1), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_WERE, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_REGEN|M1_OMNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE|M2_HUMAN|M2_COLLECT, M3_INFRAVISIBLE, CLR_RED),
Monster("werewolf", S_HUMAN, 5, 12, 10, 20, -7, (1), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_WERE, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_REGEN|M1_OMNIVORE, M2_NOPOLY|M2_WERE|M2_HOSTILE|M2_HUMAN|M2_COLLECT, M3_INFRAVISIBLE, CLR_ORANGE),
Monster("elf", S_HUMAN, 10, 12, 10, 2, -3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_NOPOLY|M2_ELF|M2_STRONG|M2_COLLECT, M3_INFRAVISION|M3_INFRAVISIBLE, CLR_WHITE),
Monster("Woodland-elf", S_HUMAN, 4, 12, 10, 10, -5, (G_GENO|G_SGROUP|2), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_ELF|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GREEN),
Monster("Green-elf", S_HUMAN, 5, 12, 10, 10, -6, (G_GENO|G_SGROUP|2), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_ELF|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BRIGHT_GREEN),
Monster("Grey-elf", S_HUMAN, 6, 12, 10, 10, -7, (G_GENO|G_SGROUP|2), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_ELF|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("elf-lord", S_HUMAN, 8, 12, 10, 20, -9, (G_GENO|G_SGROUP|2), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_ELF|M2_STRONG|M2_LORD|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BRIGHT_BLUE),
Monster("Elvenking", S_HUMAN, 9, 12, 10, 25, -10, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None], 800, 350, 0, MS_HUMANOID, MZ_HUMAN, MR_SLEEP, MR_SLEEP, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS, M2_ELF|M2_STRONG|M2_PRINCE|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("doppelganger", S_HUMAN, 9, 12, 5, 20, 0, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 12), None, None, None, None, None], 1450, 400, 0, MS_IMITATE, MZ_HUMAN, MR_SLEEP, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("nurse", S_HUMAN, 11, 6, 0, 0, 0, (G_GENO|3), [Attack(AT_CLAW, AD_HEAL, 2, 6), None, None, None, None, None], 1450, 400, 0, MS_NURSE, MZ_HUMAN, MR_POISON, MR_POISON, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_HOSTILE, M3_INFRAVISIBLE, CLR_WHITE),
Monster("shopkeeper", S_HUMAN, 12, 18, 0, 50, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 4, 4), Attack(AT_WEAP, AD_PHYS, 4, 4), None, None, None, None], 1450, 400, None, MS_SELL, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("guard", S_HUMAN, 12, 12, 10, 40, 10, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 4,10), None, None, None, None, None], 1450, 400, None, MS_GUARD, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_BLUE),
Monster("prisoner", S_HUMAN, 12, 12, 10, 0, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_DJINNI, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE|M3_CLOSE, CLR_WHITE),
Monster("Oracle", S_HUMAN, 12, 0, 0, 50, 0, (G_NOGEN|G_UNIQ), [Attack(AT_NONE, AD_MAGM, 0, 4), None, None, None, None, None], 1450, 400, 0, MS_ORACLE, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_FEMALE, M3_INFRAVISIBLE, CLR_BRIGHT_BLUE),
Monster("aligned priest", S_HUMAN, 12, 12, 10, 50, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 4,10), Attack(AT_KICK, AD_PHYS, 1, 4), Attack(AT_MAGC, AD_CLRC, 0, 0), None, None, None], 1450, 400, None, MS_PRIEST, MZ_HUMAN, MR_ELEC, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_LORD|M2_PEACEFUL|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("high priest", S_HUMAN, 25, 15, 7, 70, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 4,10), Attack(AT_KICK, AD_PHYS, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), None, None], 1450, 400, None, MS_PRIEST, MZ_HUMAN, MR_FIRE|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_HUMANOID|M1_SEE_INVIS|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MINION|M2_PRINCE|M2_NASTY|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("soldier", S_HUMAN, 6, 10, 10, 0, -2, (G_SGROUP|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_GRAY),
Monster("sergeant", S_HUMAN, 8, 10, 10, 5, -3, (G_SGROUP|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_RED),
Monster("lieutenant", S_HUMAN, 10, 10, 10, 15, -4, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 3, 4), Attack(AT_WEAP, AD_PHYS, 3, 4), None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_GREEN),
Monster("captain", S_HUMAN, 12, 10, 10, 15, -5, (G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 4, 4), Attack(AT_WEAP, AD_PHYS, 4, 4), None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_BLUE),
Monster("watchman", S_HUMAN, 6, 10, 10, 0, -2, (G_SGROUP|G_NOGEN|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_GRAY),
Monster("watch captain", S_HUMAN, 10, 10, 10, 15, -4, (G_NOGEN|G_GENO|1), [Attack(AT_WEAP, AD_PHYS, 3, 4), Attack(AT_WEAP, AD_PHYS, 3, 4), None, None, None, None], 1450, 400, 0, MS_SOLDIER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_MERC|M2_STALK|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_GREEN),
Monster("Medusa", S_HUMAN, 20, 12, 2, 50, -15, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_GAZE, AD_STON, 0, 0), Attack(AT_BITE, AD_DRST, 1, 6), None, None], 1450, 400, 0, MS_HISS, MZ_LARGE, MR_POISON|MR_STONE, MR_POISON|MR_STONE, M1_FLY|M1_SWIM|M1_AMPHIBIOUS|M1_HUMANOID|M1_POIS|M1_OMNIVORE, M2_NOPOLY|M2_HOSTILE|M2_STRONG|M2_PNAME|M2_FEMALE, M3_WAITFORU|M3_INFRAVISIBLE, CLR_BRIGHT_GREEN),
Monster("Wizard of Yendor", S_HUMAN, 30, 12, -8, 100, -128, (G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_SAMU, 2,12), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1450, 400, 0, MS_CUSS, MZ_HUMAN, MR_FIRE|MR_POISON, MR_FIRE|MR_POISON, M1_FLY|M1_BREATHLESS|M1_HUMANOID|M1_REGEN|M1_SEE_INVIS|M1_TPORT| M1_TPORT_CNTRL|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_HOSTILE|M2_STRONG|M2_NASTY| M2_PRINCE|M2_MALE|M2_MAGIC, M3_COVETOUS|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Croesus", S_HUMAN, 20, 15, 0, 40, 15, (G_UNIQ|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 4,10), None, None, None, None, None], 1450, 400, 0, MS_GUARD, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_SEE_INVIS|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_PNAME| M2_PRINCE|M2_MALE|M2_GREEDY|M2_JEWELS|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("ghost", S_GHOST, 10, 3, -5, 50, -5, (G_NOCORPSE|G_NOGEN), [Attack(AT_TUCH, AD_PHYS, 1, 1), None, None, None, None, None], 1450, 0, 0, MS_SILENT, MZ_HUMAN, MR_COLD|MR_DISINT|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_WALLWALK|M1_HUMANOID|M1_UNSOLID, M2_NOPOLY|M2_UNDEAD|M2_STALK|M2_HOSTILE, M3_INFRAVISION, CLR_GRAY),
Monster("shade", S_GHOST, 12, 10, 10, 0, 0, (G_NOCORPSE|G_NOGEN), [Attack(AT_TUCH, AD_PLYS, 2, 6), Attack(AT_TUCH, AD_SLOW, 1, 6), None, None, None, None], 1450, 0, 0, MS_WAIL, MZ_HUMAN, MR_COLD|MR_DISINT|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_BREATHLESS|M1_WALLWALK|M1_HUMANOID|M1_UNSOLID|M1_SEE_INVIS, M2_NOPOLY|M2_UNDEAD|M2_WANDER|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISION, CLR_BLACK),
Monster("water demon", S_DEMON, 8, 12,-4, 30, -7, (G_NOCORPSE|G_NOGEN), [Attack(AT_WEAP, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None], 1450, 400, 0, MS_DJINNI, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_POIS|M1_SWIM, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BLUE),
Monster("horned devil", S_DEMON, 6, 9, -5, 50, 11, (G_HELL|G_NOCORPSE|2), [Attack(AT_WEAP, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_BITE, AD_PHYS, 2, 3), Attack(AT_STNG, AD_PHYS, 1, 3), None, None], 1450, 400, 0, MS_SILENT, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_POIS|M1_THICK_HIDE, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_BROWN),
Monster("succubus", S_DEMON, 6, 12, 0, 70, -9, (G_NOCORPSE|1), [Attack(AT_BITE, AD_SSEX, 0, 0), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), None, None, None], 1450, 400, 0, MS_SEDUCE, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_FLY|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_FEMALE, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("incubus", S_DEMON, 6, 12, 0, 70, -9, (G_NOCORPSE|1), [Attack(AT_BITE, AD_SSEX, 0, 0), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), None, None, None], 1450, 400, 0, MS_SEDUCE, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_FLY|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_MALE, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("erinys", S_DEMON, 7, 12, 2, 30, 10, (G_HELL|G_NOCORPSE|G_SGROUP|2), [Attack(AT_WEAP, AD_DRST, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_SILENT, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_FEMALE| M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("barbed devil", S_DEMON, 8, 12, 0, 35, 8, (G_HELL|G_NOCORPSE|G_SGROUP|2), [Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_STNG, AD_PHYS, 3, 4), None, None, None], 1450, 400, 0, MS_SILENT, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_POIS|M1_THICK_HIDE, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("marilith", S_DEMON, 7, 12, -6, 80, -12, (G_HELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_WEAP, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4)], 1450, 400, 0, MS_CUSS, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_SLITHY|M1_SEE_INVIS|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("vrock", S_DEMON, 8, 12, 0, 50, -9, (G_HELL|G_NOCORPSE|G_SGROUP|2), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_BITE, AD_PHYS, 1, 6), None], 1450, 400, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("hezrou", S_DEMON, 9, 6, -2, 55, -10, (G_HELL|G_NOCORPSE|G_SGROUP|2), [Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_CLAW, AD_PHYS, 1, 3), Attack(AT_BITE, AD_PHYS, 4, 4), None, None, None], 1450, 400, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("bone devil", S_DEMON, 9, 15, -1, 40, -9, (G_HELL|G_NOCORPSE|G_SGROUP|2), [Attack(AT_WEAP, AD_PHYS, 3, 4), Attack(AT_STNG, AD_DRST, 2, 4), None, None, None, None], 1450, 400, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("ice devil", S_DEMON, 11, 6, -4, 55, -12, (G_HELL|G_NOCORPSE|2), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_BITE, AD_PHYS, 2, 4), Attack(AT_STNG, AD_COLD, 3, 4), None, None], 1450, 400, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_COLD|MR_POISON, 0, M1_SEE_INVIS|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_WHITE),
Monster("nalfeshnee", S_DEMON, 11, 9, -1, 65, -11, (G_HELL|G_NOCORPSE|1), [Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_CLAW, AD_PHYS, 1, 4), Attack(AT_BITE, AD_PHYS, 2, 4), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None], 1450, 400, 0, MS_SPELL, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_HUMANOID|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("pit fiend", S_DEMON, 13, 6, -3, 65, -13, (G_HELL|G_NOCORPSE|2), [Attack(AT_WEAP, AD_PHYS, 4, 2), Attack(AT_WEAP, AD_PHYS, 4, 2), Attack(AT_HUGS, AD_PHYS, 2, 4), None, None, None], 1450, 400, 0, MS_GROWL, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_SEE_INVIS|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("balrog", S_DEMON, 16, 5, -2, 75, -14, (G_HELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 8, 4), Attack(AT_WEAP, AD_PHYS, 4, 6), None, None, None, None], 1450, 400, 0, MS_SILENT, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_DEMON|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_RED),
Monster("Juiblex", S_DEMON, 50, 3, -7, 65, -15, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_ENGL, AD_DISE, 4,10), Attack(AT_SPIT, AD_ACID, 3, 6), None, None, None, None], 1500, 0, 0, MS_GURGLE, MZ_LARGE, MR_FIRE|MR_POISON|MR_ACID|MR_STONE, 0, M1_AMPHIBIOUS|M1_AMORPHOUS|M1_NOHEAD|M1_FLY|M1_SEE_INVIS|M1_ACID| M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY|M2_LORD| M2_MALE, M3_WAITFORU|M3_WANTSAMUL|M3_INFRAVISION, CLR_BRIGHT_GREEN),
Monster("Yeenoghu", S_DEMON, 56, 18, -5, 80, -15, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 3, 6), Attack(AT_WEAP, AD_CONF, 2, 8), Attack(AT_CLAW, AD_PLYS, 1, 6), Attack(AT_MAGC, AD_MAGM, 2, 6), None, None], 900, 500, 0, MS_ORC, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY|M2_LORD| M2_MALE|M2_COLLECT, M3_WANTSAMUL|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Orcus", S_DEMON, 66, 9, -6, 85, -20, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 3, 6), Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_CLAW, AD_PHYS, 3, 4), Attack(AT_MAGC, AD_SPEL, 8, 6), Attack(AT_STNG, AD_DRST, 2, 4), None], 1500, 500, 0, MS_ORC, MZ_HUGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY|M2_PRINCE| M2_MALE|M2_COLLECT, M3_WAITFORU|M3_WANTSBOOK|M3_WANTSAMUL|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Geryon", S_DEMON, 72, 3, -3, 75, 15, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_PHYS, 3, 6), Attack(AT_CLAW, AD_PHYS, 3, 6), Attack(AT_STNG, AD_DRST, 2, 4), None, None, None], 1500, 500, 0, MS_BRIBE, MZ_HUGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS|M1_SLITHY, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY| M2_PRINCE|M2_MALE, M3_WANTSAMUL|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Dispater", S_DEMON, 78, 15, -2, 80, 15, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 4, 6), Attack(AT_MAGC, AD_SPEL, 6, 6), None, None, None, None], 1500, 500, 0, MS_BRIBE, MZ_HUMAN, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS|M1_HUMANOID, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY| M2_PRINCE|M2_MALE|M2_COLLECT, M3_WANTSAMUL|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Baalzebub", S_DEMON, 89, 9, -5, 85, 20, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_BITE, AD_DRST, 2, 6), Attack(AT_GAZE, AD_STUN, 2, 6), None, None, None, None], 1500, 500, 0, MS_BRIBE, MZ_LARGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY| M2_PRINCE|M2_MALE, M3_WANTSAMUL|M3_WAITFORU|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Asmodeus", S_DEMON, 105, 12, -7, 90, 20, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_PHYS, 4, 4), Attack(AT_MAGC, AD_COLD, 6, 6), None, None, None, None], 1500, 500, 0, MS_BRIBE, MZ_HUGE, MR_FIRE|MR_COLD|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_HUMANOID|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_STRONG| M2_NASTY|M2_PRINCE|M2_MALE, M3_WANTSAMUL|M3_WAITFORU|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Demogorgon", S_DEMON, 106, 15, -8, 95, -20, (G_HELL|G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_MAGC, AD_SPEL, 8, 6), Attack(AT_STNG, AD_DRLI, 1, 4), Attack(AT_CLAW, AD_DISE, 1, 6), Attack(AT_CLAW, AD_DISE, 1, 6), None, None], 1500, 500, 0, MS_GROWL, MZ_HUGE, MR_FIRE|MR_POISON, 0, M1_FLY|M1_SEE_INVIS|M1_NOHANDS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_PNAME|M2_NASTY| M2_PRINCE|M2_MALE, M3_WANTSAMUL|M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Death", S_DEMON, 30, 12, -5, 100, 0, (G_UNIQ|G_NOGEN), [Attack(AT_TUCH, AD_DETH, 8, 8), Attack(AT_TUCH, AD_DETH, 8, 8), None, None, None, None], 1450, 1, 0, MS_RIDER, MZ_HUMAN, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_HUMANOID|M1_REGEN|M1_SEE_INVIS|M1_TPORT_CNTRL, M2_NOPOLY|M2_STALK|M2_HOSTILE|M2_PNAME|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Pestilence", S_DEMON, 30, 12, -5, 100, 0, (G_UNIQ|G_NOGEN), [Attack(AT_TUCH, AD_PEST, 8, 8), Attack(AT_TUCH, AD_PEST, 8, 8), None, None, None, None], 1450, 1, 0, MS_RIDER, MZ_HUMAN, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_HUMANOID|M1_REGEN|M1_SEE_INVIS|M1_TPORT_CNTRL, M2_NOPOLY|M2_STALK|M2_HOSTILE|M2_PNAME|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("Famine", S_DEMON, 30, 12, -5, 100, 0, (G_UNIQ|G_NOGEN), [Attack(AT_TUCH, AD_FAMN, 8, 8), Attack(AT_TUCH, AD_FAMN, 8, 8), None, None, None, None], 1450, 1, 0, MS_RIDER, MZ_HUMAN, MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_STONE, 0, M1_FLY|M1_HUMANOID|M1_REGEN|M1_SEE_INVIS|M1_TPORT_CNTRL, M2_NOPOLY|M2_STALK|M2_HOSTILE|M2_PNAME|M2_STRONG|M2_NASTY, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_MAGENTA),
Monster("djinni", S_DEMON, 7, 12, 4, 30, 0, (G_NOGEN|G_NOCORPSE), [Attack(AT_WEAP, AD_PHYS, 2, 8), None, None, None, None, None], 1500, 400, 0, MS_DJINNI, MZ_HUMAN, MR_POISON|MR_STONE, 0, M1_HUMANOID|M1_FLY|M1_POIS, M2_NOPOLY|M2_STALK|M2_COLLECT, M3_INFRAVISIBLE, CLR_YELLOW),
Monster("sandestin", S_DEMON, 13, 12, 4, 60, -5, (G_HELL|G_NOCORPSE|1), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_WEAP, AD_PHYS, 2, 6), None, None, None, None], 1500, 400, 0, MS_CUSS, MZ_HUMAN, MR_STONE, 0, M1_HUMANOID, M2_NOPOLY|M2_STALK|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE|M3_INFRAVISION, CLR_GRAY),
Monster("jellyfish", S_EEL, 3, 3, 6, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_STNG, AD_DRST, 3, 3), None, None, None, None, None], 80, 20, 0, MS_SILENT, MZ_SMALL, MR_POISON, MR_POISON, M1_SWIM|M1_AMPHIBIOUS|M1_SLITHY|M1_NOLIMBS|M1_NOTAKE|M1_POIS, M2_HOSTILE, 0, CLR_BLUE),
Monster("piranha", S_EEL, 5, 12, 4, 0, 0, (G_GENO|G_NOGEN|G_SGROUP), [Attack(AT_BITE, AD_PHYS, 2, 6), None, None, None, None, None], 60, 30, 0, MS_SILENT, MZ_SMALL, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_SLITHY|M1_NOLIMBS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, 0, CLR_RED),
Monster("shark", S_EEL, 7, 12, 2, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_BITE, AD_PHYS, 5, 6), None, None, None, None, None], 500, 350, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_SLITHY|M1_NOLIMBS| M1_CARNIVORE|M1_OVIPAROUS|M1_THICK_HIDE|M1_NOTAKE, M2_HOSTILE, 0, CLR_GRAY),
Monster("giant eel", S_EEL, 5, 9, -1, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_BITE, AD_PHYS, 3, 6), Attack(AT_TUCH, AD_WRAP, 0, 0), None, None, None, None], 200, 250, 0, MS_SILENT, MZ_HUGE, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_SLITHY|M1_NOLIMBS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_CYAN),
Monster("electric eel", S_EEL, 7, 10, -3, 0, 0, (G_GENO|G_NOGEN), [Attack(AT_BITE, AD_ELEC, 4, 6), Attack(AT_TUCH, AD_WRAP, 0, 0), None, None, None, None], 200, 250, 0, MS_SILENT, MZ_HUGE, MR_ELEC, MR_ELEC, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_SLITHY|M1_NOLIMBS| M1_CARNIVORE|M1_OVIPAROUS|M1_NOTAKE, M2_HOSTILE, M3_INFRAVISIBLE, CLR_BRIGHT_BLUE),
Monster("kraken", S_EEL, 20, 3, 6, 0, -3, (G_GENO|G_NOGEN), [Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_HUGS, AD_WRAP, 2, 6), Attack(AT_BITE, AD_PHYS, 5, 4), None, None], 1800, 1000, 0, MS_SILENT, MZ_HUGE, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_NOPOLY|M2_HOSTILE|M2_STRONG, M3_INFRAVISIBLE, CLR_RED),
Monster("newt", S_LIZARD, 0, 6, 8, 0, 0, (G_GENO|5), [Attack(AT_BITE, AD_PHYS, 1, 2), None, None, None, None, None], 10, 20, 0, MS_SILENT, MZ_TINY, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_YELLOW),
Monster("gecko", S_LIZARD, 1, 6, 8, 0, 0, (G_GENO|5), [Attack(AT_BITE, AD_PHYS, 1, 3), None, None, None, None, None], 10, 20, 0, MS_SQEEK, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_GREEN),
Monster("iguana", S_LIZARD, 2, 6, 7, 0, 0, (G_GENO|5), [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 30, 30, 0, MS_SILENT, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BROWN),
Monster("baby crocodile", S_LIZARD, 3, 6, 7, 0, 0, G_GENO, [Attack(AT_BITE, AD_PHYS, 1, 4), None, None, None, None, None], 200, 200, 0, MS_SILENT, MZ_MEDIUM, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_BROWN),
Monster("lizard", S_LIZARD, 5, 6, 6, 10, 0, (G_GENO|5), [Attack(AT_BITE, AD_PHYS, 1, 6), None, None, None, None, None], 10, 40, 0, MS_SILENT, MZ_TINY, MR_STONE, MR_STONE, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_HOSTILE, 0, CLR_GREEN),
Monster("chameleon", S_LIZARD, 6, 5, 6, 10, 0, (G_GENO|2), [Attack(AT_BITE, AD_PHYS, 4, 2), None, None, None, None, None], 100, 100, 0, MS_SILENT, MZ_TINY, 0, 0, M1_ANIMAL|M1_NOHANDS|M1_CARNIVORE, M2_NOPOLY|M2_HOSTILE, 0, CLR_BROWN),
Monster("crocodile", S_LIZARD, 6, 9, 5, 0, 0, (G_GENO|1), [Attack(AT_BITE, AD_PHYS, 4, 2), Attack(AT_CLAW, AD_PHYS, 1,12), None, None, None, None], 1450, 400, 0, MS_SILENT, MZ_LARGE, 0, 0, M1_SWIM|M1_AMPHIBIOUS|M1_ANIMAL|M1_THICK_HIDE|M1_NOHANDS| M1_OVIPAROUS|M1_CARNIVORE, M2_STRONG|M2_HOSTILE, 0, CLR_BROWN),
Monster("salamander", S_LIZARD, 8, 12, -1, 0, -9, (G_HELL|1), [Attack(AT_WEAP, AD_PHYS, 2, 8), Attack(AT_TUCH, AD_FIRE, 1, 6), Attack(AT_HUGS, AD_PHYS, 2, 6), Attack(AT_HUGS, AD_FIRE, 3, 6), None, None], 1500, 400, 0, MS_MUMBLE, MZ_HUMAN, MR_SLEEP|MR_FIRE, MR_FIRE, M1_HUMANOID|M1_SLITHY|M1_THICK_HIDE|M1_POIS, M2_STALK|M2_HOSTILE|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_ORANGE),
Monster("long worm tail", S_WORM_TAIL, 0, 0, 0, 0, 0, (G_NOGEN|G_NOCORPSE|G_UNIQ), [None, None, None, None, None, None], 0, 0, 0, 0, 0, 0, 0, 0L, M2_NOPOLY, 0, CLR_BROWN),
Monster("archeologist", S_HUMAN, 10, 12, 10, 1, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_TUNNEL|M1_NEEDPICK|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("barbarian", S_HUMAN, 10, 12, 10, 1, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("caveman", S_HUMAN, 10, 12, 10, 0, 1, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("cavewoman", S_HUMAN, 10, 12, 10, 0, 1, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("healer", S_HUMAN, 10, 12, 10, 1, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("knight", S_HUMAN, 10, 12, 10, 1, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("monk", S_HUMAN, 10, 12, 10, 2, 0, G_NOGEN, [Attack(AT_CLAW, AD_PHYS, 1, 8), Attack(AT_KICK, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_HERBIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT|M2_MALE, M3_INFRAVISIBLE, CLR_WHITE),
Monster("priest", S_HUMAN, 10, 12, 10, 2, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_MALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("priestess", S_HUMAN, 10, 12, 10, 2, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("ranger", S_HUMAN, 10, 12, 10, 2, -3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 4), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("rogue", S_HUMAN, 10, 12, 10, 1, -3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_GREEDY|M2_JEWELS|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("samurai", S_HUMAN, 10, 12, 10, 1, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("tourist", S_HUMAN, 10, 12, 10, 1, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("valkyrie", S_HUMAN, 10, 12, 10, 1, -1, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, MR_COLD, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_FEMALE|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("wizard", S_HUMAN, 10, 12, 10, 3, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_WHITE),
Monster("Lord Carnarvon", S_HUMAN, 20, 12, 0, 30, 20, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_TUNNEL|M1_NEEDPICK|M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Pelias", S_HUMAN, 20, 12, 0, 30, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Shaman Karnov", S_HUMAN, 20, 12, 0, 30, 20, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Hippocrates", S_HUMAN, 20, 12, 0, 40, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("King Arthur", S_HUMAN, 20, 12, 0, 40, 20, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Grand Master", S_HUMAN, 25, 12, 0, 70, 0, (G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_PHYS, 4, 10), Attack(AT_KICK, AD_PHYS, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_FIRE|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_HUMANOID|M1_SEE_INVIS|M1_HERBIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_NASTY|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_BLACK),
Monster("Arch Priest", S_HUMAN, 25, 12, 7, 70, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 4,10), Attack(AT_KICK, AD_PHYS, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), Attack(AT_MAGC, AD_CLRC, 2, 8), None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_FIRE|MR_ELEC|MR_SLEEP|MR_POISON, 0, M1_HUMANOID|M1_SEE_INVIS|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_WHITE),
Monster("Orion", S_HUMAN, 20, 12, 0, 30, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE|M1_SEE_INVIS|M1_SWIM|M1_AMPHIBIOUS, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISION|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Master of Thieves", S_HUMAN, 20, 12, 0, 30, -20, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_SAMU, 2, 4), None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_MALE|M2_GREEDY| M2_JEWELS|M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Lord Sato", S_HUMAN, 20, 12, 0, 30, 20, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Twoflower", S_HUMAN, 20, 12, 10, 20, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_PEACEFUL|M2_STRONG|M2_MALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_WHITE),
Monster("Norn", S_HUMAN, 20, 12, 0, 80, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, MR_COLD, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_FEMALE| M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Neferet the Green", S_HUMAN, 20, 12, 0, 60, 0, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_MAGC, AD_SPEL, 2, 8), None, None, None, None], 1450, 400, 0, MS_LEADER, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_FEMALE|M2_PNAME|M2_PEACEFUL| M2_STRONG|M2_COLLECT|M2_MAGIC, M3_CLOSE|M3_INFRAVISIBLE, CLR_GREEN),
Monster("Minion of Huhetotl", S_DEMON, 16, 12, -2, 75, -14, (G_NOCORPSE|G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 8, 4), Attack(AT_WEAP, AD_PHYS, 4, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None], 1450, 400, 0, MS_NEMESIS, MZ_LARGE, MR_FIRE|MR_POISON|MR_STONE, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_STALK|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_COLLECT, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISION|M3_INFRAVISIBLE, CLR_RED),
Monster("Thoth Amon", S_HUMAN, 16, 12, 0, 10, -14, (G_NOGEN|G_UNIQ|G_NOCORPSE), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_SAMU, 1, 4), None, None], 1450, 400, 0, MS_NEMESIS, MZ_HUMAN, MR_POISON|MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_STRONG|M2_MALE|M2_STALK|M2_HOSTILE| M2_NASTY|M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Chromatic Dragon", S_DRAGON, 16, 12, 0, 30, -14, (G_NOGEN|G_UNIQ), [Attack(AT_BREA, AD_RBRE, 6, 8), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_SAMU, 2, 8), Attack(AT_BITE, AD_PHYS, 4, 8), Attack(AT_BITE, AD_PHYS, 4, 8), Attack(AT_STNG, AD_PHYS, 1, 6)], 4500, 1700, 0, MS_NEMESIS, MZ_GIGANTIC, MR_FIRE|MR_COLD|MR_SLEEP|MR_DISINT|MR_ELEC|MR_POISON|MR_ACID|MR_STONE, MR_FIRE|MR_COLD|MR_SLEEP|MR_DISINT|MR_ELEC|MR_POISON|MR_STONE, M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_HOSTILE|M2_FEMALE|M2_STALK|M2_STRONG|M2_NASTY| M2_GREEDY|M2_JEWELS|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Cyclops", S_GIANT, 18, 12, 0, 0, -15, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 4, 8), Attack(AT_WEAP, AD_PHYS, 4, 8), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None, None], 1900, 700, 0, MS_NEMESIS, MZ_HUGE, MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_GIANT|M2_STRONG|M2_ROCKTHROW|M2_STALK|M2_HOSTILE| M2_NASTY|M2_MALE|M2_JEWELS|M2_COLLECT, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISION|M3_INFRAVISIBLE, CLR_GRAY),
Monster("Ixoth", S_DRAGON, 15, 12, -1, 20, -14, (G_NOGEN|G_UNIQ), [Attack(AT_BREA, AD_FIRE, 8, 6), Attack(AT_BITE, AD_PHYS, 4, 8), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_PHYS, 2, 4), Attack(AT_CLAW, AD_SAMU, 2, 4), None ], 4500, 1600, 0, MS_NEMESIS, MZ_GIGANTIC, MR_FIRE|MR_STONE, MR_FIRE, M1_FLY|M1_THICK_HIDE|M1_NOHANDS|M1_CARNIVORE|M1_SEE_INVIS, M2_NOPOLY|M2_PNAME|M2_HOSTILE|M2_STRONG|M2_NASTY|M2_STALK| M2_GREEDY|M2_JEWELS|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_RED),
Monster("Master Kaen", S_HUMAN, 25, 12, -10, 10, -20, (G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_PHYS, 16, 2), Attack(AT_CLAW, AD_PHYS, 16, 2), Attack(AT_MAGC, AD_CLRC, 0, 0), Attack(AT_CLAW, AD_SAMU, 1, 4), None, None], 1450, 400, 0, MS_NEMESIS, MZ_HUMAN, MR_POISON|MR_STONE, MR_POISON, M1_HUMANOID|M1_HERBIVORE|M1_SEE_INVIS, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_HOSTILE|M2_STRONG|M2_NASTY| M2_STALK|M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Nalzok", S_DEMON, 16, 12, -2, 85, -127, (G_NOGEN|G_UNIQ|G_NOCORPSE), [Attack(AT_WEAP, AD_PHYS, 8, 4), Attack(AT_WEAP, AD_PHYS, 4, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None], 1450, 400, 0, MS_NEMESIS, MZ_LARGE, MR_FIRE|MR_POISON|MR_STONE, 0, M1_FLY|M1_SEE_INVIS|M1_POIS, M2_NOPOLY|M2_DEMON|M2_PNAME|M2_HOSTILE|M2_STRONG|M2_STALK| M2_NASTY|M2_COLLECT, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISION|M3_INFRAVISIBLE, CLR_RED),
Monster("Scorpius", S_SPIDER, 15, 12, 10, 0, -15, (G_NOGEN|G_UNIQ), [Attack(AT_CLAW, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_SAMU, 2, 6), Attack(AT_STNG, AD_DISE, 1, 4), None, None, None], 750, 350, 0, MS_NEMESIS, MZ_HUMAN, MR_POISON|MR_STONE, MR_POISON, M1_ANIMAL|M1_NOHANDS|M1_OVIPAROUS|M1_POIS|M1_CARNIVORE, M2_NOPOLY|M2_PNAME|M2_HOSTILE|M2_STRONG|M2_STALK|M2_NASTY| M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU, CLR_MAGENTA),
Monster("Master Assassin", S_HUMAN, 15, 12, 0, 30, 18, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_DRST, 2, 6), Attack(AT_WEAP, AD_PHYS, 2, 8), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None, None], 1450, 400, 0, MS_NEMESIS, MZ_HUMAN, MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_HOSTILE|M2_STALK|M2_NASTY| M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Ashikaga Takauji", S_HUMAN, 15, 12, 0, 40, -13, (G_NOGEN|G_UNIQ|G_NOCORPSE), [Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_WEAP, AD_PHYS, 2, 6), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None, None], 1450, 400, 0, MS_NEMESIS, MZ_HUMAN, MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PNAME|M2_HOSTILE|M2_STRONG|M2_STALK| M2_NASTY|M2_MALE|M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Lord Surtur", S_GIANT, 15, 12, 2, 50, 12, (G_NOGEN|G_UNIQ), [Attack(AT_WEAP, AD_PHYS, 2,10), Attack(AT_WEAP, AD_PHYS, 2,10), Attack(AT_CLAW, AD_SAMU, 2, 6), None, None, None], 2250, 850, 0, MS_NEMESIS, MZ_HUGE, MR_FIRE|MR_STONE, MR_FIRE, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_GIANT|M2_MALE|M2_PNAME|M2_HOSTILE|M2_STALK| M2_STRONG|M2_NASTY|M2_ROCKTHROW|M2_JEWELS|M2_COLLECT, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISION|M3_INFRAVISIBLE, CLR_MAGENTA),
Monster("Dark One", S_HUMAN, 15, 12, 0, 80, -10, (G_NOGEN|G_UNIQ|G_NOCORPSE), [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_CLAW, AD_SAMU, 1, 4), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None], 1450, 400, 0, MS_NEMESIS, MZ_HUMAN, MR_STONE, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_STRONG|M2_HOSTILE|M2_STALK|M2_NASTY| M2_COLLECT|M2_MAGIC, M3_WANTSARTI|M3_WAITFORU|M3_INFRAVISIBLE, CLR_BLACK),
Monster("student", S_HUMAN, 5, 12, 10, 10, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_TUNNEL|M1_NEEDPICK|M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("chieftain", S_HUMAN, 5, 12, 10, 10, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("neanderthal", S_HUMAN, 5, 12, 10, 10, 1, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 2, 4), None, None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("attendant", S_HUMAN, 5, 12, 10, 10, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, MR_POISON, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("page", S_HUMAN, 5, 12, 10, 10, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("abbot", S_HUMAN, 5, 12, 10, 20, 0, G_NOGEN, [Attack(AT_CLAW, AD_PHYS, 8, 2), Attack(AT_KICK, AD_STUN, 3, 2), Attack(AT_MAGC, AD_CLRC, 0, 0), None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_HERBIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("acolyte", S_HUMAN, 5, 12, 10, 20, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_MAGC, AD_CLRC, 0, 0), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("hunter", S_HUMAN, 5, 12, 10, 10, -7, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 4), None, None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_SEE_INVIS|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISION|M3_INFRAVISIBLE, CLR_WHITE),
Monster("thug", S_HUMAN, 5, 12, 10, 10, -3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_WEAP, AD_PHYS, 1, 6), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_GREEDY|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("ninja", S_HUMAN, 5, 12, 10, 10, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_HUMANOID, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_HOSTILE|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("roshi", S_HUMAN, 5, 12, 10, 10, 3, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT, M3_INFRAVISIBLE, CLR_WHITE),
Monster("warrior", S_HUMAN, 5, 12, 10, 10, -1, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 8), Attack(AT_WEAP, AD_PHYS, 1, 8), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT|M2_FEMALE, M3_INFRAVISIBLE, CLR_WHITE),
Monster("apprentice", S_HUMAN, 5, 12, 10, 30, 0, G_NOGEN, [Attack(AT_WEAP, AD_PHYS, 1, 6), Attack(AT_MAGC, AD_SPEL, 0, 0), None, None, None, None], 1450, 400, 0, MS_GUARDIAN, MZ_HUMAN, 0, 0, M1_HUMANOID|M1_OMNIVORE, M2_NOPOLY|M2_HUMAN|M2_PEACEFUL|M2_STRONG|M2_COLLECT|M2_MAGIC, M3_INFRAVISIBLE, CLR_WHITE),
)

# }}}

# monsters_where {{{

@queryable
def monsters_where():
    return monsters

# }}}
# by_ {{{

by_glyph = defaultdict(list)
map(lambda m:by_glyph[m.get_glyph()].append(m), monsters)

by_appearance = defaultdict(list)
map(lambda m:by_appearance[m.appearance].append(m), monsters)

# }}}
