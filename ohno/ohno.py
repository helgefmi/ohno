from __future__ import absolute_import

import random
import time

from loglady import LogLady

from ohno.client.client import Client
from ohno.framebuffer import FrameBuffer
from ohno.ui.ui import UI
from ohno.hero import Hero
from ohno.dungeon.dungeon import Dungeon
from ohno.ai.ai import AI
from ohno.messages import Messages

class Ohno(object):
    """
    The root object. Every subpart of ohno can be found through this class.
    """
    def __init__(self, root_dir):
        # Make sure __init__ doesn't do any crazy stuff.
        # Should always make sure initializing Ohno won't throw any exceptions.
        self.logger = LogLady(root_dir + '/logs', \
            ('ohno', 'client', 'telnet', 'framebuffer', 'hero', 'dungeon', \
             'ui', 'curses', 'input', 'pty', 'strategy', 'action', 'tile',
             'level', 'messages'))

        # Every submodule needs to be able to find other submodules, so they
        # all take an ohno instance as the first argument.
        self.client = Client(self)
        self.framebuffer = FrameBuffer(self)
        self.ui = UI(self)
        self.hero = Hero(self)
        self.dungeon = Dungeon(self)
        self.ai = AI(self)
        self.messages = Messages(self)

        self.paused = self.running = None
        self.last_action = None
        self.tick = 0

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
        while self.running:
            # First, take input from the client and update our framebuffer.
            # This should always leave the client in a state where _doing stuff_
            # is possioble (that is, not in a menu, no --More-- messages, etc.)
            # Any messages sent to us is stored in `messages` temporarily,
            # because we want to update the hero and dungeon before sending them
            # to ohno.messages.
            messages = self.framebuffer.update()
            # Updates stats like hp, ac, hunger, score, dlvl
            self.hero.update()
            # Creates new level and/or updates the level with what we got from
            # framebuffer.
            self.dungeon.update()

            # Start parsing the messages
            for message in filter(len, messages):
                self.messages.new_message(message)

            # Update the user display and/or take input from the user.
            self.ui.update()
            # Search the level once. This is then cached for fast queries by the
            # AI later on.
            self.ai.pathing.search()

            # Some actiosn might want to do something depending on the outcome
            # of an action (example: what happened when I read the unidentified
            # scroll?)
            if self.last_action:
                self.last_action.done()

            while self.running and self.paused:
                time.sleep(0.01)
                self.ui.update()

            # Ask the AI for the next action and send the key strokes needed for
            # that action.
            self.logger.ohno('Getting the next action from `strategy`..')
            action = self.ai.strategy.next_action()
            command = action.get_command()
            self.logger.ohno('Got action: %r (%r)!' % (action, command))
            self.client.send(command)

            # Internal tick used by ai.pathing as a sanity check.
            self.tick += 1

            self.last_action = action

    def shutdown(self):
        """Shuts ohno down without saving. You should probably use .save() instead."""
        self.ui.shutdown() # Curses
        self.running = False

    def save(self):
        """Tries to save the game and then runs .shutdown()"""
        self.client.send('\x1b\x1b\x1b\x1bSyq')
        self.shutdown()
