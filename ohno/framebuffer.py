from __future__ import absolute_import

import re

from ansiterm import Ansiterm

from ohno.appearance import Appearance
from ohno.event.discovery import Discovery
from ohno.event.founditems import FoundItems
from ohno.event.youdie import YouDie
from ohno.point import Point

class FrameBuffer(object):
    """
    Wraps around `ansiterm`, and includes nethack specific functions to make
    life easier.
    It's also in control of fetching from our client and updating the state of
    ohno (see update())
    """
    split_messages = re.compile(' \s+')
    find_discoveries = re.compile('^(.*?) \((.*?)\)$')

    def __init__(self, ohno):
        self.ohno = ohno
        self.ansiterm = Ansiterm(24, 80)

    def _parse_things_that_are_here(self):
        self.ohno.logger.framebuffer('Parsing "Things that are here"..')
        things = []
        while True:
            screen = self.get_string()

            if '--More--' not in screen:
                break

            if screen.index('--More--') / 80 == 0:
                break

            try:
                # First iteration
                start_pos = screen.index('Things that are here:')
                assert things == []
                self.ohno.logger.framebuffer('[TTAH] first iteration')
                start_x = start_pos % 80
                start_y = start_pos / 80 + 1
            except ValueError:
                # Next iterations
                assert start_x
                self.ohno.logger.framebuffer('[TTAH] second iteration')
                start_y = 0
                
            end_y = screen.index('--More--') / 80
            for y in xrange(start_y, end_y):
                pos = y * 80 + start_x
                end_pos = screen.index('  ', pos)
                # In case the text hugs the right border.
                end_pos = min(end_pos, y * 80 + 80)

                thing = screen[y * 80 + start_x:end_pos]
                things.append(thing)

            self.ohno.client.send(' ')
            self.feed(self.ohno.client.receive())

        self.ohno.logger.framebuffer('Things that is here: %r' % things)
        return things

    def _parse_discoveries(self):
        self.ohno.logger.framebuffer('Parsing discoveries..')
        discoveries = []
        start_pos = self.get_string().index('Discoveries')
        start_x = start_pos % 80
        start_y = start_pos / 80 + 2
        while '--More--' in self.get_string():
            screen = self.get_string()
            end_pos = self.get_string().index('--More--')
            for y in xrange(start_y, end_pos / 80):
                from_pos = y * 80 + start_x
                to_pos = y * 80 + 80
                line = screen[from_pos:to_pos]
                if line[1] != ' ':
                    continue
                assert line[2] != ' '
                line = line[2:].strip()
                match = FrameBuffer.find_discoveries.match(line)
                assert match, line
                identity, appearance = match.groups()
                discoveries += [(appearance, identity)]

            self.ohno.client.send(' ')
            self.feed(self.ohno.client.receive())

        self.ohno.logger.framebuffer('Discoveries: %s' % discoveries)
        return discoveries

    def _read_messages(self, receive_first=True):
        self.ohno.logger.framebuffer('Reading messages..')
        messages = ''
        first_iter = True
        while True:
            if not first_iter or receive_first:
                # Read from the client update the framebuffer
                data = self.ohno.client.receive()
                self.feed(data)
            first_iter = False

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

        messages = messages.replace('--More--', '  ').strip()
        ret = FrameBuffer.split_messages.split(messages)
        if ret == ['']:
            return []
        return ret

    def update(self):
        """
        This function initially gets called by Ohno.loop, and should not return 
        from that call untill the bot is in a state of needing an action (i.e.
        menus should be closed, no --More-- in topline, no "What do you want to
        wish for?" etc.
        """
        self.ohno.logger.framebuffer('Updating framebuffer..')

        messages = self._read_messages()
        
        if 'Discoveries' in messages:
            # We should only get this when there's no other messages.
            assert len(messages) == 1
            discoveries = self._parse_discoveries()
            for appearance, identity in discoveries:
                Discovery.fire(self.ohno, appearance, identity)

        if 'Things that are here:' in self.get_string():
            things = self._parse_things_that_are_here()
            FoundItems.fire(self.ohno, things)
            # Since we're not synchronized at this moment (there might be an
            # unparsed topline after calling _parse_things_that_are_here), we
            # must call _read_messages again.
            messages += self._read_messages(receive_first=False)

        self.ohno.logger.framebuffer('All messages: %r' % messages)

        for message in messages:
            if (message.startswith('Do you want your possessions ') or 
               message.startswith('Do you want to see what you had ') or
               message.startswith('You die.')):
                YouDie.fire(self.ohno, messages)
                assert False, "Some event should probably exit()"

            # TODO
            #if message.startswith('Call a ') or message.startswith('Call an'):
            #    self.ohno.client.send('\n')
            #    return messages + self.update()

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
