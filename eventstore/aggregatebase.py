import uuid
from abc import abstractmethod
from methoddispatch import SingleDispatch
from typing import List
from .event import Event


class AggregateBase(SingleDispatch):

    _pending_events = []
    version: int = -1

    @abstractmethod
    def correlation_id(self) -> str:
        pass

    def apply_event(self, event: Event):
        self.apply(event)
        event.command_id = str(uuid.uuid4())
        self.version += 1

    def raise_event(self, event: Event):
        self.apply_event(event)
        self._pending_events.append(event)

    async def clear_pending_events(self):
        self._pending_events.clear()

    @property
    def pending_events(self) -> List[Event]:
        return self._pending_events

