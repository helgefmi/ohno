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

    def update(self):
        """
        1. Read from the client
        2. Gather messages and press space and goto 1. if we get
           a "--More--" message
        3. TODO: handle menus
        4. Return the messages so `Ohno` can handle them.

        This function initially gets called by Ohno.loop, and should not return 
        from that call untill the bot is in a state of needing an action (i.e.
        menus should be closed, no --More-- in topline, no "What do you want to
        wish for?" etc.
        """
        self.ohno.logger.framebuffer('Updating framebuffer..')

        messages = ''
        while True:
            data = self.ohno.client.receive()
            self.feed(data)

            messages += self.get_topline()

            # TODO: Hmm. Apparantely we can get a --More-- on the second line
            #       aswell (using the pty client.)
            if '--More--' in messages:
                # double space so we can split on it later
                messages = messages.replace('--More--', '  ')
                # There's more messages in store for us!
                self.ohno.client.send(' ')
            else:
                break

        messages = FrameBuffer.split_messages.split(messages.strip(' '))
        self.ohno.logger.framebuffer('All messages: ' + 
                                     (', '.join(map(repr, messages))))
        
        return messages
