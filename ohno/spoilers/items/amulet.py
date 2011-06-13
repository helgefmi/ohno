def items():
    appearances = map(
        "{0} amulet".format,
        ('circular spherical oval triangular pyramidal square concave hexagonal'
         ' octagonal').split()
    )

    amulets = {
        'Amulet of Yendor' : {
            'price':  30000,
            'artifact':  1,
            'fullname':  'The Amulet of Yendor',
            'appearance':  'Amulet of Yendor',
            'material':  'mithril',
        },

        'Eye of the Aethiopica' : {
            'price':  4000,
            'edible':  1,
            'artifact':  1,
            'fullname':  'The Eye of the Aethiopica',
            'base':  'amulet of ESP',
            'material':  'iron',
        },

        'cheap plastic imitation of the Amulet of Yendor' : {
            'price':  0,
            'appearance':  'Amulet of Yendor',
            'material':  'plastic',
        },

        'amulet of change' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet of ESP' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet of life saving' : {
            'material':  'iron',
        },
        'amulet of magical breathing' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet of reflection' : {
            'material':  'iron',
        },
        'amulet of restful sleep' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet of strangulation' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet of unchanging' : {
            'edible':  1,
            'material':  'iron',
        },
        'amulet versus poison' : {
            'edible':  1,
            'material':  'iron',
        },
    }

    return amulets, {
        'weight':  20,
        'price':  150,
        'appearances':  appearances,
        'glyph':  '"',
    }
