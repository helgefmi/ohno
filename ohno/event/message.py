from ohno.event.baseevent import BaseEvent

class MessageEvent(BaseEvent):
    def __init__(self, ohno, msgtype, msg):
        super(MessageEvent, self).__init__(ohno)
        self.msgtype = msgtype
        self.msg = msg
