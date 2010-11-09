from ohno import config
from ohno.client.telnet import Telnet

class Client():
    """Wraps around a specific NetHack client (telnet, /usr/bin/nethack, ..)"""
    def __init__(self, ohno):
        self.ohno = ohno

        if config.CLIENT == 'telnet':
            self.ohno.logger.client('Initializing telnet client')
            self._client = Telnet(ohno)
        else:
            self.ohno.logger.client('Initializing nethack client')
            self._client = Nethack(ohno)

    def start_resume_game(self):
        """
        Starts or resumes a nethack game and leaves the game in a state
        such that we can start running ohno.senses.update()
        """
        self.ohno.logger.client('Starting/resuming game..')
        return self._client.start_resume_game()

    def send(self, data):
        self.ohno.logger.client('> ' + repr(data))
        return self._client.send(data)

    def receive(self):
        self.ohno.logger.client('Calling receive() on client..')
        data = self._client.receive()
        self.ohno.logger.client('< ' + repr(data))
        return data
