from __future__ import absolute_import

import time

from loglady import LogLady

from ohno import util
from ohno.ai.ai import AI
from ohno.client.client import Client
from ohno.dungeon.dungeon import Dungeon
from ohno.event.founditems import FoundItems
from ohno.event.message import MessageEvent
from ohno.event.youdie import YouDie
from ohno.framebuffer import FrameBuffer
from ohno.hero import Hero
from ohno.messages import Messages
from ohno.spoilers.spoilers import Spoilers
from ohno.ui.ui import UI

class Ohno(object):
    """
    The root object. Every subpart of ohno can be found through this class.
    """
    def __init__(self, root_dir):
        # Make sure __init__ doesn't do any crazy stuff.
        # Should always make sure initializing Ohno won't throw any exceptions.
        self.logger = LogLady(root_dir + '/logs',
            ('ohno', 'client', 'telnet', 'framebuffer', 'hero', 'dungeon',
             'ui', 'curses', 'input', 'pty', 'strategy', 'action', 'tile',
             'level', 'messages', 'event', 'monster', 'spoilers', 'item'))

        # Every submodule needs to be able to find other submodules, so they
        # all take an ohno instance as the first argument.
        self.client = Client(self)
        self.framebuffer = FrameBuffer(self)
        self.ui = UI(self)
        self.hero = Hero(self)
        self.dungeon = Dungeon(self)
        self.ai = AI(self)
        self.messages = Messages(self)
        self.spoilers = Spoilers(self)

        self.paused = self.running = None
        self.last_action = None
        self.tick = 0
        self.all_messages = []

        YouDie.subscribe(self.on_youdie)
        MessageEvent.subscribe(self.on_message)

    def start_resume_game(self):
        """Starts or resumes a nethack game within the current client."""
        self.logger.ohno('Starting/resuming game..')
        self.client.start_resume_game()

    def loop(self):
        """
        The main controller of ohno. Makes sure everything happens in the
        correct order.
        """
        self.running = True
        self.paused = False
        first = True
        while self.running:
            # First, take input from the client and update our framebuffer.
            # This should always leave the client in a state where _doing stuff_
            # is possible (that is, not in a menu, no --More-- messages, etc.)
            # Any messages sent to us is stored in `messages` temporarily,
            # because we want to update the hero and dungeon before sending them
            # to ohno.messages.
            messages = self.framebuffer.update()
            self.all_messages.extend(messages)

            # framebuffer.update() might shut us down if we're dead.
            if not self.running:
                break

            # Updates stats (bottomlines) and hero's position.
            self.hero.update()

            # Creates new level and/or updates the level with what we got from
            # framebuffer.
            self.dungeon.update()

            # Update ohno about the current game (inventory, discoveries, etc.)
            # the first pass through this loop.
            if first:
                first = False
                messages += self.look()
                self.discoveries()

            # Start parsing the messages
            for message in messages:
                if message: self.messages.parse_message(message)

            # Update the user display and/or take input from the user.
            self.ui.update()

            # Some actions might want to do something depending on the outcome
            # of an action (example: what happened when I read the unidentified
            # scroll?). This could be used for sanity checks aswell.
            if self.last_action:
                self.last_action.done()

            # Ask the AI for the next action and send the key strokes needed for
            # that action.
            self.logger.ohno('Getting the next action from `strategy`..')
            action = self.ai.strategy.next_action()
            command = action.get_command()
            self.logger.ohno('Got action: %r (%r)!' % (action, command))
            self.client.send(command)

            while self.running and self.paused:
                time.sleep(0.01)
                self.ui.update()

            # Internal tick used by ai.pathing as a sanity check.
            self.tick += 1

            self.last_action = action

    def shutdown(self):
        """
        Shuts ohno down without saving.
        You should probably use .save() instead.
        """
        self.ui.shutdown() # Curses
        self.running = False

    def save(self):
        """Tries to save the game and then runs .shutdown()"""
        self.client.send('\x1b\x1b\x1b\x1bSyq')
        self.shutdown()

    # actions
    def farlook(self, to_tile):
        from_tile = self.dungeon.curtile
        x1, y1 = from_tile.idx % 80, from_tile.idx / 80
        x2, y2 = to_tile.idx % 80, to_tile.idx / 80
        sequence = util.farlook(x1, y1, x2, y2)
        self.client.send(';%s.' % sequence)
        messages = self.framebuffer.update()
        assert len(messages) == 2
        return messages[1]

    def discoveries(self):
        self.client.send('\\')
        self.framebuffer.update()

    def look(self):
        self.client.send(':')
        return self.framebuffer.update()

    # events
    def on_youdie(self, event):
        self.logger.ohno('Seems like we\'re dead. Shutting down.')
        self.shutdown()
        print '\n'.join(event.messages)
        print 'I died. Sorry!'
        exit(0)

    def on_message(self, event):
        if event.msgtype == 'you_see_here':
            thing = event.kwargs['item']
            FoundItems.fire(self, [thing])
