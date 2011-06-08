from __future__ import absolute_import

import re

from ansiterm import Ansiterm

from ohno.appearance import Appearance

class FrameBuffer(object):
    """
    Wraps around `ansiterm`, and includes nethack specific functions to make
    life easier.
    It's also in control of fetching from our client and updating the state of
    ohno (see update())
    """
    split_messages = re.compile(' \s+')
    def __init__(self, ohno):
        self.ohno = ohno
        self.ansiterm = Ansiterm(24, 80)

    def feed(self, data):
        return self.ansiterm.feed(data)

    def get_topline(self):
        return self.ansiterm.get_string(0, 80)

    def get_bottomlines(self):
        return self.ansiterm.get_string(80 * 22, 80 * 24)

    def get_string(self):
        return self.ansiterm.get_string(0, 80 * 24)

    def get_maptiles(self):
        """
        Returns a list of the map tiles (line 2 to and incl. 22). The tiles are
        stored as a dict. Layout of a tile: {
            'glyph': char,
            'color': {
                'fg': int,
                'bg': int,
                'bold': bool,
                'reverse': bool
            }
        }
        """
        return [Appearance(tile.glyph, tile.color)
                    for tile in self.ansiterm.get_tiles(80, 80 * 22)]

    def get_cursor(self):
        cursor = self.ansiterm.get_cursor()
        return (int(cursor['y']), int(cursor['x']))

    def parse_things_that_are_here(self):
        string = self.get_string()

        start_pos = string.index('Things that are here:')
        start_x = start_pos % 80
        start_y = start_pos / 80

        things = []
        for y in xrange(start_y + 1, 25):
            pos = y * 80 + start_x
            end_pos = string.index('  ', pos)
            if end_pos >= y * 80 + 80:
                end_pos = y * 80 + 80

            thing = string[y * 80 + start_x:end_pos]
            if thing == '--More--':
                break
            things.append(thing)
        self.ohno.logger.framebuffer('Things that is here: %r' % things)
        self.ohno.client.send(' ')
        self.update()

    def update(self):
        """
        1. Read from the client
        2. Gather messages and press space and goto 1. if we get
           a "--More--" message
        3. Handle menus
        4. Return the messages so `Ohno` can handle them.

        This function initially gets called by Ohno.loop, and should not return 
        from that call untill the bot is in a state of needing an action (i.e.
        menus should be closed, no --More-- in topline, no "What do you want to
        wish for?" etc.
        """
        self.ohno.logger.framebuffer('Updating framebuffer..')

        messages = ''
        while True:
            # Read from the client update the framebuffer
            data = self.ohno.client.receive()
            self.feed(data)

            # Topline should only contain messages
            messages += self.get_topline().strip()

            if '--More--' in self.get_string():
                # Sometimes, messages will span two lines; we need to check for
                # that!
                if '--More--' not in self.get_topline():
                    endpos = self.get_string().index('--More--')
                    if self.get_string()[endpos - 1] != ' ':
                        if endpos / 80 != 1:
                            raise Exception(
                                'Got --More-- on line %s' % (endpos / 80)
                            )
                        messages += self.get_string()[80:endpos] + '  '
                    elif endpos % 80 > 0:
                        break
                # There's more messages.
                self.ohno.client.send(' ')
            else:
                break

        messages = messages.replace('--More--', '  ')
        messages = FrameBuffer.split_messages.split(messages.strip(' '))
        self.ohno.logger.framebuffer('All messages: ' + 
                                     ', '.join(map(repr, messages)))
        
        if 'Things that are here:' in self.get_string():
            self.parse_things_that_are_here()

        if 'Do you want your possessions identified? [ynq] (y)' in messages:
            self.ohno.logger.framebuffer('Seems like we\'re dead. Cya!')
            self.ohno.shutdown()
            print "You died."

        return messages
