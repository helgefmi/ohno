import socket
import time

import ohno.config as config

class Telnet():
    """A telnet client for ohno.client"""
    def __init__(self, ohno):
        self.ohno = ohno
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, data):
        return self._connection.sendall(data)

    def receive(self):
        buf = ''
        self.ohno.client.send('\xff\xfdc')
        while not buf.endswith('\xff\xfcc'):
            buf += self._connection.recv(8096)
        return buf.replace('\xff\xfcc', '')

    def start_resume_game(self):
        self.ohno.logger.telnet('Connecting to %s:%d' % config.TELNET_HOST)
        self._connection.connect(config.TELNET_HOST)
        self.ohno.logger.telnet('Telnet negotiation ..')
        self.ohno.client.send("\xff\xfb\x18\xff\xfa\x18\x00xterm-color\xff\xf0"
                              "\xff\xfc \xff\xfc#\xff\xfc'\xff\xfe\x03\xff\xfb"
                              "\x01\xff\xfd\x05\xff\xfb!\xff\xfb\x1f\xff\xfa"
                              "\x1f\x00P\x00\x18\xff\xf0")
        data = self.receive()
        assert 'Not logged in' in data
        self.ohno.logger.telnet('We have a DGL screen!')

        self.ohno.logger.telnet('Logging in as %s..' % config.DGL_CREDS[0])
        self.ohno.client.send("l%s\n%s\n" % (config.DGL_CREDS))
        data = self.receive()
        assert 'Logged in as' in data
        self.ohno.logger.telnet('Login successful!')

        del config.DGL_CREDS # because why not

        self.ohno.logger.telnet('Pressing `p` for play..')
        self.ohno.client.send('p')

        # Make sure we don't break out of the loop unless the game is in
        # a state ohno.senses.update() can deal with!
        while True:
            data = self.receive()
            if 'Shall I pick a character' in data:
                self.ohno.logger.telnet('Game not started.. Starting one!')
                self.ohno.client.send('nvd  ')
                break
            elif 'will recover in 10' in data:
                self.ohno.logger.telnet('Stale nethack processes.. '
                                        'Waiting 10 secounds.')
                time.sleep(11)
            elif 'Restoring save file' in data:
                self.ohno.logger.telnet('Previous game found, restoring..')
                self.ohno.client.send(' ')
                break
