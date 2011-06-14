from ohno.event.baseevent import BaseEvent

class FoundItems(BaseEvent):
    def __init__(self, ohno, items):
        super(FoundItems, self).__init__(ohno)
        self.items = items
