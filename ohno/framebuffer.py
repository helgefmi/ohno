from __future__ import absolute_import

import re

from ansiterm import Ansiterm

from ohno.appearance import Appearance
from ohno.point import Point

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

    def _parse_things_that_are_here(self):
        screen = self.get_string()

        start_pos = screen.index('Things that are here:')
        start_x = start_pos % 80
        start_y = start_pos / 80
        end_y = screen.index('--More--') / 80

        things = []
        for y in xrange(start_y + 1, end_y):
            pos = y * 80 + start_x
            end_pos = screen.index('  ', pos)
            # The line might take the rest of this row, in which a space will be
            # found on another row.
            end_pos = min(end_pos, y * 80 + 80)

            things.append(screen[y * 80 + start_x:end_pos])
        self.ohno.logger.framebuffer('Things that is here: %r' % things)

    def _read_messages(self):
        messages = ''
        while True:
            # Read from the client update the framebuffer
            data = self.ohno.client.receive()
            self.feed(data)

            # Topline should only contain messages
            messages += self.get_topline().strip()

            if '--More--' not in self.get_string():
                break

            # Sometimes, messages will span two lines; we must check for that!
            if '--More--' not in self.get_topline():
                endpos = self.get_string().index('--More--')
                if self.get_string()[endpos - 1] != ' ':
                    messages += self.get_string()[80:endpos] + '  '
                elif endpos % 80 > 0:
                    # There's a menu on the screen - we'll deal with that in
                    # update().
                    break

            # Read more messages
            self.ohno.client.send(' ')

        messages = messages.replace('--More--', '  ').strip(' ')
        return FrameBuffer.split_messages.split(messages)

    def update(self):
        """
        This function initially gets called by Ohno.loop, and should not return 
        from that call untill the bot is in a state of needing an action (i.e.
        menus should be closed, no --More-- in topline, no "What do you want to
        wish for?" etc.
        """
        self.ohno.logger.framebuffer('Updating framebuffer..')

        messages = self._read_messages()
        self.ohno.logger.framebuffer('All messages: %r' % messages)
        
        if 'Things that are here:' in self.get_string():
            self._parse_things_that_are_here()
            self.ohno.client.send(' ')
            return messages + self.update()

        for message in messages:
            if (message.startswith('Do you want your possessions ') or 
               message.startswith('Do you want to see what you had ') or
               message.startswith('You die')):
                self.ohno.logger.framebuffer('Seems like we\'re dead. Cya!')
                self.ohno.shutdown()
                print '\n'.join(messages)
                return

            if message.startswith('Call a ') or message.startswith('Call an'):
                self.ohno.client.send('\n')
                return messages + self.update()

        return messages

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
        return Point(int(cursor['x']), int(cursor['y']))
