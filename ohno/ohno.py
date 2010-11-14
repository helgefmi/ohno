from __future__ import absolute_import

import random
import time

from loglady import LogLady

from ohno.client.client import Client
from ohno.senses import Senses
from ohno.framebuffer import FrameBuffer
from ohno.ui.ui import UI
from ohno.hero import Hero
from ohno.dungeon.dungeon import Dungeon

class Ohno:
    """
    The root object. Every subpart of ohno can be found through this class.
    """
    def __init__(self, root_dir):
        # Make sure __init__ doesn't do any crazy stuff.
        # Should always make sure initializing Ohno won't throw any exceptions.
        self.logger = LogLady(root_dir + '/logs', \
            ('ohno', 'client', 'telnet', 'senses', 'hero', 'dungeon', \
             'ui', 'curses', 'input', 'pty'))

        # Every submodule needs to be able to find other submodules, so they
        # all take an ohno instance as the first argument.
        self.client = Client(self)
        self.senses = Senses(self)
        self.framebuffer = FrameBuffer(self)
        self.ui = UI(self)
        self.hero = Hero(self)
        self.dungeon = Dungeon(self)

        self.paused = self.running = None

    def start_resume_game(self):
        """Starts or resumes a nethack game within the current client"""
        self.logger.ohno('Starting/resuming game..')
        self.client.start_resume_game()

    def loop(self):
        """
        The main controller of ohno. Makes sure everything happens in order.
        """
        self.running = True
        self.paused = False
        while self.running:
            self.senses.update()
            self.ui.update()
            while self.paused:
                time.sleep(0.01)
                self.ui.update()

            # Temporary hack untill the bot has an AI.
            self.client.send('yubnhjkl'[random.randint(0, 7)])

    def shutdown(self):
        """Stops ohno completely. Remember to .save() first!"""
        self.ui.shutdown() # Curses
        self.running = False

    def save(self):
        """Tries to save the game and then runs .shutdown()"""
        self.client.send('\x1b\x1b\x1b\x1bSyq')
        self.shutdown()
