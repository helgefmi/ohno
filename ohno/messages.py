import re

_msgparsers = {
    "(needs food, badly!|feel weak now\.|feel weak\.)":              'is_weak',
    "There is a staircase (down|up) here":                           'is_staircase_here',
    "Your (right|left) leg is in no shape":                          'leg_no_shape',
    "Your leg feels somewhat better":                                'leg_feels_better',
    "You see here":                                                  'found_items',
    "Things that are here":                                          'found_items',
    "There are (several|many) objects here":                         'found_items',
    "There's some graffiti on the floor here":                       'graffiti_on_floor',
    'You read: "(.*?)"':                                             'graffiti_on_floor',
    "Velkommen, (^,)+!":                                             'shop_entrance',
    "There is an open door here":                                    'open_door_here',
    "There is a bear trap here|You are caught in a bear trap":       'found_beartrap',
    "You feel more confident in your ((^ )+) ":                      'skill_up',
    "You feel quick":                                                ('gain_instrinct', 'fast'),
    "You are momentarily blinded by a flash of light":               'blinded',
    "You are still in a pit|You fall into a pit":                    'fell_into_pit',
    "You are caught in a bear trap|A bear trap closes on your foot": 'stepped_in_beartrap',
    "Click! You trigger":                                            'trigger_trap',
    "There is a magic trap here":                                    ('found_trap', 'magic'),
    "There is a falling rock trap|A trap door in the ceiling opens": ('found_trap', 'rock'),
    "There is an arrow trap":                                        ('found_trap', 'arrow'),
    "A board beneath you squeaks loudly":                            ('found_trap', 'squeek'),
    "This door is locked":                                           'locked_door',
    "You get expelled":                                              'got_expelled',
    "You return to (human|) form":                                   'no_poly',
    "There is a teleportation trap here":                            ('found_trap', 'teleport'),
}
class Messages(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.msgparsers = []
        for regexp, method in _msgparsers.iteritems():
            compiled_regexp = re.compile(regexp)
            bound_method = getattr(self, method if type(method) is str else method[0])
            def _f(match):
                bound_method(*(match + method[1:] if type(method) is tuple else []))
            self.msgparsers.append((compiled_regexp, _f))

    def new_message(self, msg):
        self.ohno.logger.messages('Got message: %s' % repr(msg))
        for regexp, method in self.msgparsers:
            match = regexp.match(msg)
            self.ohno.logger.messages('Found parser: %r' % method)
            if match:
                method(match.groups())

    def found_items(self):
        assert False
    def skill_up(self):
        assert False
    def graffiti_on_floor(self):
        assert False
    def leg_feels_better(self):
        assert False
    def found_trap(self):
        assert False
    def fell_into_pit(self):
        assert False
    def shop_entrance(self):
        assert False
    def gain_instrinct(self):
        assert False
    def blinded(self):
        assert False
    def locked_door(self):
        assert False
    def is_weak(self):
        assert False
    def no_poly(self):
        assert False
    def is_staircase_here(self):
        assert False
    def leg_no_shape(self):
        assert False
    def found_beartrap(self):
        assert False
    def stepped_in_beartrap(self):
        assert False
    def open_door_here(self):
        assert False
    def trigger_trap(self):
        assert False
    def got_expelled(self):
        assert False
