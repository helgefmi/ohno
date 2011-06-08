from __future__ import absolute_import

import pty
import time
import os
import sys

class Pty(object):
    """Runs a local nethack client from a pty"""
    def __init__(self, ohno):
        self.ohno = ohno
        self.child = None

    def send(self, data):
        return os.write(self.child, data)

    def receive(self):
        time.sleep(0.03)
        ret = os.read(self.child, 4096)
        # Since we're asking for 4096 bytes, if we get that exact amount of
        # bytes, there's probably more to be read.
        # This isn't a foolproof method and is bound to fail at some point, but
        # that should be really rare.
        if len(ret) >= 4095:
            ret += os.read(self.child, 4096)
        return ret

    def start_resume_game(self):
        # Forks to make a process with a pseudo-terminal for running nethack
        # locally.
        pid, self.child = pty.fork()
        if pid == 0:
            self.ohno.logger.pty('(CHILD) Running nethack..')
            os.environ['TERM'] = 'xterm-color'
            os.environ['COLUMNS'] = '80'
            os.environ['LINES'] = '24'
            os.execv('/usr/games/nethack', [''])
            self.ohno.logger.pty('(CHILD) This should never happen.')
            sys.exit(1)
        else:
            time.sleep(0.3)
            self.ohno.logger.pty('(PARENT) Receving initial data from child..')
            data = self.receive()
            time.sleep(0.3)
            if 'Shall I pick a character' in data:
                self.ohno.logger.pty('(PARENT) Creating new character..')
                self.send('nvhl ')
            elif 'Restoring save file' in data:
                self.ohno.logger.pty('(PARENT) Resuming game..')
                self.send(' ')
            else:
                assert False
