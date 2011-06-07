from ohno.event.baseevent import BaseEvent

class MessageEvent(BaseEvent):
    def __init__(self, ohno, msgtype, kwargs):
        super(MessageEvent, self).__init__(ohno)
        self.msgtype = msgtype
        self.kwargs = kwargs
