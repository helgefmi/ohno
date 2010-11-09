from __future__ import absolute_import # else `from ohno.*` will use ohno.py as base

from loglady import LogLady

from ohno.client.client import Client
from ohno.senses import Senses
from ohno.framebuffer import FrameBuffer
from ohno.display import Display
from ohno.hero import Hero
from ohno.dungeon.dungeon import Dungeon

class Ohno:
    def __init__(self, ROOT_DIR):
        # Make sure __init__ doesn't do any crazy stuff.
        # Should always make sure initializing Ohno won't throw any exceptions.
        self.logger = LogLady(ROOT_DIR + '/logs', ('ohno', 'client', 'telnet', 'senses', 'hero', 'dungeon', 'display'))

        self.client = Client(self)
        self.senses = Senses(self)
        self.framebuffer = FrameBuffer(self)
        self.display = Display(self)
        self.hero = Hero(self)
        self.dungeon = Dungeon(self)

    def start_resume_game(self):
        self.logger.ohno('Starting/resuming game..')
        self.client.start_resume_game()

    def loop(self):
        self.running = True
        while self.running:
            self.senses.update()
            self.display.update()

            # Temporary hack untill the bot has an AI.
            import time
            time.sleep(0.5)

    def shutdown(self):
        # Called from the main binary file.
        self.display.shutdown() # Curses
        self.running = False

    def save(self):
        self.client.send('\x1b\x1b\x1b\x1bSyq')
        self.shutdown()
