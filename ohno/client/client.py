from ohno import config
from ohno.client.telnet import Telnet

class Client():
    def __init__(self, ohno):
        self.ohno = ohno
        if config.CLIENT == 'telnet':
            self.ohno.logger.client('Initializing telnet client')
            self._client = Telnet(ohno)
        else:
            self.ohno.logger.client('Initializing nethack client')
            self._client = Nethack(ohno)

    def start_resume_game(self):
        self.ohno.logger.client('Starting/resuming game..')
        return self._client.start_resume_game()

    def send(self, data):
        self.ohno.logger.client('Sending: ' + repr(data))
        return self._client.send(data)

    def receive(self):
        self.ohno.logger.client('Calling receive() on client..')
        data = self._client.receive()
        self.ohno.logger.client('Receiving: ' + repr(data))
        return data
