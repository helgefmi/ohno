from ohno.event.baseevent import BaseEvent

class YouDie(BaseEvent):
    def __init__(self, ohno, messages=None):
        super(YouDie, self).__init__(ohno)
        self.messages = messages
