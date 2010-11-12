from __future__ import absolute_import

import pty
import time
import os
import sys

import ohno.config as config

class Pty():
    def __init__(self, ohno):
        self.ohno = ohno

    def send(self, data):
        return os.write(self.child, data)

    def receive(self):
        time.sleep(0.1)
        ret = os.read(self.child, 4096)
        if len(ret) >= 4095:
            ret += os.read(self.child, 4096)
        return ret

    def start_resume_game(self):
        pid, self.child = pty.fork()
        if pid == 0:
            self.ohno.logger.pty('(CHILD) Running nethack..')
            os.environ['TERM'] = 'xterm-color'
            os.environ['COLUMNS'] = '80'
            os.environ['LINES'] = '24'
            os.execv('/usr/games/nethack', [''])
            self.ohno.logger.pty('(CHILD) This should never happen.')
            os.exit(1)
        else:
            time.sleep(0.3)
            self.ohno.logger.pty('(PARENT) Receving initial data from child..')
            data = self.receive()
            if 'Shall I pick a character' in data:
                self.ohno.logger.pty('(PARENT) Creating new character..')
                self.send('nvd ')
            elif 'Restoring save file' in data:
                self.ohno.logger.pty('(PARENT) Resuming game..')
                self.send(' ')
            else:
                assert False
