from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from src.domain.shared.event.event_interface import EventInterface

TEventInterface = TypeVar("TEventInterface", bound="EventInterface")


class EventHandlerInterface(ABC, Generic[TEventInterface]):

    @abstractmethod
    def handle(self, event: TEventInterface):
        raise NotImplementedError
