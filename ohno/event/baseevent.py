class BaseEvent(object):
    """
    The baseclass of ohno's event system.

    The subclasses can be used as interactive instances (e.g. different
    handlers can vote on which item to wish for in WishEvent), and the
    subscribing/fireing of events is all handled in BaseEvent.

    Instead of creating your own Event instances, use
    EventClass.fire(*args, **kwargs), which will do that for you, let the
    handlers handle the event, and then return it to the caller.
    """
    def __init__(self, ohno):
        self.ohno = ohno

    @classmethod
    def subscribe(cls, handler):
        """
        Adds a handler to the event class.
        """
        assert cls is not BaseEvent

        # We'll make the handlers list when someone subscribs for the first
        # time, so we won't have to worry about having one in each subclass.
        if not hasattr(cls, '_handlers'):
            cls._handlers = []

        if hasattr(handler, '__iter__'):
            cls._handlers.extend(handler)
        else:
            cls._handlers.append(handler)

    @classmethod
    def unsubscribe(cls, handler):
        cls._handlers.remove(handler)

    @classmethod
    def fire(cls, ohno, *args, **kwargs):
        """
        Create an instance of the event, sends it to all the handlers, and
        returns the event.
        """
        if not hasattr(cls, '_handlers'):
            raise Exception('Tried to fire an event with no handlers')

        event = cls(ohno, *args, **kwargs)
        ohno.logger.event('Fireing event %r' % event)
        for handler in cls._handlers:
            handler(event)
        return event
