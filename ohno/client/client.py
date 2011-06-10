from ohno import config
from ohno.client.telnet import Telnet
from ohno.client.pty import Pty

class Client(object):
    """Wraps around a specific NetHack client (telnet, /usr/bin/nethack, ..)"""
    def __init__(self, ohno):
        self.ohno = ohno

        if config.CLIENT == 'telnet':
            self.ohno.logger.client('Initializing telnet client')
            self._client = Telnet(ohno)
        elif config.CLIENT == 'pty':
            self.ohno.logger.client('Initializing nethack client')
            self._client = Pty(ohno)
        else:
            raise Exception('config.CLIENT?')

    def start_resume_game(self):
        """
        Starts or resumes a nethack game and leaves the game in a state
        such that we can start running ohno.senses.update()
        """
        self.ohno.logger.client('Starting/resuming game..')
        self._client.start_resume_game()
        self.ohno.logger.client('Game should be started/resumed.')

    def send(self, data, **kwargs):
        self.ohno.logger.client('> ' + repr(data))
        return self._client.send(data, **kwargs)

    def receive(self, **kwargs):
        self.ohno.logger.client('Calling receive() on client..')
        data = self._client.receive(**kwargs)
        self.ohno.logger.client('< ' + repr(data))
        return data
