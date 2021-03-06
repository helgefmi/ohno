def items(spoilers):
    appearances = map('scroll labeled {0}'.format, [
        'ZELGO MER', 'JUYED AWK YACC', 'NR 9', 'XIXAXA XOXAXA XUXAXA',
        'PRATYAVAYAH', 'DAIYEN FOOELS', 'LEP GEX VEN ZEA', 'PRIRUTSENIE',
        'ELBIB YLOH', 'TEMOV', 'VERR YED HORRE', 'VENZAR BORGAVVE', 'THARR',
        'YUM YUM', 'KERNOD WEL', 'ELAM EBOW', 'DUAM XNAHT', 'KIRJE',
        'ANDOVA BEGARIN', 'VE FORBRYDERNE', 'HACKEM MUCHE', 'VELOX NEB',
        'READ ME', 'FOOBIE BLETCH', 'GARVEN DEH',
    ])

    scrolls = {
        'scroll of mail' : {
            'price':  0,
            'ink':  2,
            'appearance':  'stamped scroll',
        },
        'scroll of blank paper' : {
            'price':  60,
            'ink':  0,
            'appearance':  'unlabeled scroll',
        },

        'scroll of identify' : {
            'price':  20,
            'ink':  14,
        },

        'scroll of light' : {
            'price':  50,
            'ink':  8,
        },

        'scroll of enchant weapon' : {
            'price':  60,
            'ink':  16,
        },

        'scroll of enchant armor' : {
            'price':  80,
            'ink':  16,
        },
        'scroll of remove curse' : {
            'price':  80,
            'ink':  16,
        },

        'scroll of confuse monster' : {
            'price':  100,
            'ink':  12,
        },
        'scroll of destroy armor' : {
            'price':  100,
            'ink':  10,
        },
        'scroll of fire' : {
            'price':  100,
            'ink':  8,
        },
        'scroll of food detection' : {
            'price':  100,
            'ink':  8,
        },
        'scroll of gold detection' : {
            'price':  100,
            'ink':  8,
        },
        'scroll of magic mapping' : {
            'price':  100,
            'ink':  8,
        },
        'scroll of scare monster' : {
            'price':  100,
            'ink':  20,
        },
        'scroll of teleportation' : {
            'price':  100,
            'ink':  20,
        },

        'scroll of amnesia' : {
            'price':  200,
            'ink':  8,
        },
        'scroll of create monster' : {
            'price':  200,
            'ink':  10,
        },
        'scroll of earth' : {
            'price':  200,
            'ink':  8,
        },
        'scroll of taming' : {
            'price':  200,
            'ink':  20,
        },

        'scroll of charging' : {
            'price':  300,
            'ink':  16,
        },
        'scroll of genocide' : {
            'price':  300,
            'ink':  30,
        },
        'scroll of punishment' : {
            'price':  300,
            'ink':  10,
        },
        'scroll of stinking cloud' : {
            'price':  300,
            'ink':  20,
        },
    }

    for name in scrolls:
        scrolls[name]['plural'] = name.replace('scroll', 'scrolls')

    return scrolls, {
        'weight':  5,
        'appearances':  appearances,
        'stackable':  1,
        'material':  'paper',
        'glyph':  '?',
    }
