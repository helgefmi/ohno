import re

_msgparsers = {
    "^This door is locked":                                          'locked_door',
}
class Messages(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.msgparsers = []
        for regexp, method in _msgparsers.iteritems():
            compiled_regexp = re.compile(regexp)
            method_name = method[0] if type(method) is tuple else method
            args = method[1:] if type(method) is tuple and len(method) > 1 else []
            self.msgparsers.append((compiled_regexp, method_name, args))

    def new_message(self, msg):
        self.ohno.logger.messages('Got message: %s' % repr(msg))
        for regexp, method_name, args in self.msgparsers:
            match = regexp.match(msg)
            if match:
                args = list(match.groups()) + list(args)
                self.ohno.logger.messages('Found match: name=%r args=%r' % (method_name, args))
                getattr(self, method_name)(*args)
                break
        else:
            self.ohno.logger.messages('TODO: Unparsed message %r' % msg)

    def noop(self):
        pass
    def locked_door(self):
        assert not self.ohno.last_action.tile.feature.locked
        self.ohno.last_action.tile.feature.locked = True

    def found_items(self):
        pass
    def skill_up(self):
        pass
    def graffiti_on_floor(self):
        pass
    def leg_feels_better(self):
        pass
    def found_trap(self):
        pass
    def fell_into_pit(self):
        pass
    def shop_entrance(self):
        pass
    def gain_instrinct(self):
        pass
    def blinded(self):
        pass
    def is_weak(self):
        pass
    def no_poly(self):
        pass
    def is_staircase_here(self):
        pass
    def leg_no_shape(self):
        pass
    def found_beartrap(self):
        pass
    def stepped_in_beartrap(self):
        pass
    def open_door_here(self):
        pass
    def trigger_trap(self):
        pass
    def got_expelled(self):
        pass
