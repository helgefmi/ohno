from ohno.event.baseevent import BaseEvent

class Discovery(BaseEvent):
    def __init__(self, ohno, appearance, identity):
        super(Discovery, self).__init__(ohno)
        self.appearance = appearance
        self.identity = identity
