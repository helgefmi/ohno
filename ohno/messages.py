from __future__ import absolute_import

import re

from ohno.event.message import MessageEvent

class Messages(object):
    _msgparsers = {
        "^This door is locked": 'locked_door',
    }
    def __init__(self, ohno):
        self.ohno = ohno
        self.compiled_parsers = []
        for regexp, msgtype in Messages._msgparsers.iteritems():
            compiled_regexp = re.compile(regexp)
            self.compiled_parsers.append((compiled_regexp, msgtype))

    def parse_message(self, msg):
        """
        Checks if we have a parser for this particular message, and fires a
        MessageEvent when we have a match.
        """
        self.ohno.logger.messages('Got message: %s' % repr(msg))
        for regexp, msgtype in self.compiled_parsers:
            if regexp.match(msg):
                self.ohno.logger.messages('Found match: msgtype=%r' % msgtype)
                MessageEvent.fire(self.ohno, msgtype, msg)
                break
        else:
            self.ohno.logger.messages('TODO: Unparsed message %r' % msg)
