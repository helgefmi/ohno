import re

_msgparsers = {
    "^This door is locked": 'locked_door',
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
        """
        Checks if we have a parser for this particular message, and executes
        the callback associated with this message if it matches
        """
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

    def locked_door(self):
        assert not self.ohno.last_action.tile.feature.locked
        self.ohno.last_action.tile.feature.locked = True
