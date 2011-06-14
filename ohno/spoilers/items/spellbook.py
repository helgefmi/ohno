def items():
    appearances = (
        ('parchment vellum ragged mottled stained cloth leather white pink red'
         ' orange yellow velvet turquoise cyan indigo magenta purple violet'
         ' tan plaid gray wrinkled dusty bronze copper silver gold'
         ' glittering shining dull thin thick').split() + [
            'dog eared',
            'light green',
            'dark green',
            'light blue',
            'dark blue',
            'light brown',
            'dark brown',
        ]
    )

    spellbooks = {
        'Book of the Dead' : {
            'artifact':  1,
            'price':  10000,
            'weight':  20,
            'level':  7,
            'time':  0,
            'ink':  0,
            'fullname':  'The Book of the Dead',
            'appearance':  'papyrus spellbook',
            'emergency':  0,
        },

        'spellbook of blank paper' : {
            'price':  0,
            'level':  0,
            'time':  0,
            'ink':  0,
            'appearance':  'plain spellbook',
            'emergency':  0,
        },

        'spellbook of force bolt' : {
            'price':  100,
            'level':  1,
            'time':  2,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of drain life' : {
            'price':  200,
            'level':  2,
            'time':  2,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of magic missile' : {
            'price':  200,
            'level':  2,
            'time':  2,
            'ink':  20,
            'role':  'Wiz',
            'emergency':  0,
        },
        'spellbook of cone of cold' : {
            'price':  400,
            'level':  4,
            'time':  21,
            'ink':  40,
            'role':  'Val',
            'emergency':  0,
        },
        'spellbook of fireball' : {
            'price':  400,
            'level':  4,
            'time':  12,
            'ink':  40,
            'emergency':  0,
        },
        'spellbook of finger of death' : {
            'price':  700,
            'level':  7,
            'time':  80,
            'ink':  70,
            'emergency':  0,
        },
        'spellbook of healing' : {
            'price':  100,
            'level':  1,
            'time':  2,
            'ink':  10,
            'emergency':  1,
        },
        'spellbook of cure blindness' : {
            'price':  200,
            'level':  2,
            'time':  2,
            'ink':  20,
            'emergency':  1,
        },
        'spellbook of cure sickness' : {
            'price':  300,
            'level':  3,
            'time':  6,
            'ink':  30,
            'role':  'Hea',
            'emergency':  1,
        },
        'spellbook of extra healing' : {
            'price':  300,
            'level':  3,
            'time':  10,
            'ink':  30,
            'emergency':  1,
        },
        'spellbook of stone to flesh' : {
            'price':  300,
            'level':  3,
            'time':  2,
            'ink':  30,
            'emergency':  0,
        },
        'spellbook of restore ability' : {
            'price':  400,
            'level':  4,
            'time':  15,
            'ink':  40,
            'role':  'Mon',
            'emergency':  1,
        },
        'spellbook of detect monsters' : {
            'price':  100,
            'level':  1,
            'time':  1,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of light' : {
            'price':  100,
            'level':  1,
            'time':  1,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of detect food' : {
            'price':  200,
            'level':  2,
            'time':  3,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of clairvoyance' : {
            'price':  300,
            'level':  3,
            'time':  6,
            'ink':  30,
            'role':  'Sam',
            'emergency':  0,
        },
        'spellbook of detect unseen' : {
            'price':  300,
            'level':  3,
            'time':  8,
            'ink':  30,
            'emergency':  0,
        },
        'spellbook of identify' : {
            'price':  300,
            'level':  3,
            'time':  12,
            'ink':  30,
            'emergency':  0,
        },
        'spellbook of detect treasure' : {
            'price':  400,
            'level':  4,
            'time':  15,
            'ink':  40,
            'role':  'Rog',
            'emergency':  0,
        },
        'spellbook of magic mapping' : {
            'price':  500,
            'level':  5,
            'time':  35,
            'ink':  50,
            'role':  'Arc',
            'emergency':  0,
        },
        'spellbook of sleep' : {
            'price':  100,
            'level':  1,
            'time':  1,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of confuse monster' : {
            'price':  200,
            'level':  2,
            'time':  2,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of slow monster' : {
            'price':  200,
            'level':  2,
            'time':  2,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of cause fear' : {
            'price':  300,
            'level':  3,
            'time':  6,
            'ink':  30,
            'emergency':  0,
        },
        'spellbook of charm monster' : {
            'price':  300,
            'level':  3,
            'time':  6,
            'ink':  30,
            'role':  'Tou',
            'emergency':  0,
        },
        'spellbook of protection' : {
            'price':  100,
            'level':  1,
            'time':  3,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of create monster' : {
            'price':  200,
            'level':  2,
            'time':  3,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of remove curse' : {
            'price':  300,
            'level':  3,
            'time':  10,
            'ink':  30,
            'role':  'Pri',
            'emergency':  1,
        },
        'spellbook of create familiar' : {
            'price':  600,
            'level':  6,
            'time':  42,
            'ink':  60,
            'emergency':  0,
        },
        'spellbook of turn undead' : {
            'price':  600,
            'level':  6,
            'time':  48,
            'ink':  60,
            'role':  'Kni',
            'emergency':  0,
        },
        'spellbook of jumping' : {
            'price':  100,
            'level':  1,
            'time':  3,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of haste self' : {
            'price':  300,
            'level':  3,
            'time':  8,
            'ink':  30,
            'role':  'Bar',
            'emergency':  0,
        },
        'spellbook of invisibility' : {
            'price':  400,
            'level':  4,
            'time':  15,
            'ink':  40,
            'role':  'Ran',
            'emergency':  0,
        },
        'spellbook of levitation' : {
            'price':  400,
            'level':  4,
            'time':  12,
            'ink':  40,
            'emergency':  0,
        },
        'spellbook of teleport away' : {
            'price':  600,
            'level':  6,
            'time':  36,
            'ink':  60,
            'emergency':  0,
        },
        'spellbook of knock' : {
            'price':  100,
            'level':  1,
            'time':  1,
            'ink':  10,
            'emergency':  0,
        },
        'spellbook of wizard lock' : {
            'price':  200,
            'level':  2,
            'time':  3,
            'ink':  20,
            'emergency':  0,
        },
        'spellbook of dig' : {
            'price':  500,
            'level':  5,
            'time':  30,
            'ink':  50,
            'role':  'Cav',
            'emergency':  0,
        },
        'spellbook of polymorph' : {
            'price':  600,
            'level':  6,
            'time':  48,
            'ink':  60,
            'emergency':  0,
        },
        'spellbook of cancellation' : {
            'price':  700,
            'level':  7,
            'time':  64,
            'ink':  70,
            'emergency':  0,
        },
    }

    return spellbooks, {
        'weight':  50,
        'material':  'paper',
        'glyph':  '+',
        'appearances':  appearances,
    }