from __future__ import absolute_import

from loglady import LogLady

from ohno.client.client import Client
from ohno.senses import Senses
from ohno.framebuffer import FrameBuffer
from ohno.display import Display
from ohno.hero import Hero
from ohno.dungeon.dungeon import Dungeon

class Ohno:
    def __init__(self, ROOT_DIR):
        self.logger = LogLady(ROOT_DIR + '/logs', ('ohno', 'client', 'telnet', 'senses', 'hero', 'dungeon', 'display'))

        self.client = Client(self)
        self.senses = Senses(self)
        self.framebuffer = FrameBuffer(self)
        self.display = Display(self)
        self.hero = Hero(self)
        self.dungeon = Dungeon(self)

        self.logger.ohno('Starting/resuming game..')

    def start(self):
        self.client.start_resume_game()

    def loop(self):
        while True:
            self.senses.update()
            self.display.update()

            import time
            time.sleep(0.5)

    def shutdown(self):
        self.display.shutdown()
