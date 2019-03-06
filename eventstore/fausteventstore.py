from .eventstore import  EventStore


class FaustEventStore(eventstore):

    def __init__(self):
        super().__init__()
