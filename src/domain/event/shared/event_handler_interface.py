from typing import TypeVar
from abc import ABC, abstractmethod
from src.domain.event.shared.event_interface import EventInterface

TEventInterface = TypeVar("TEventInterface", bound="EventInterface")


class EventHandlerInterface(ABC):

    @abstractmethod
    def handle(self, event: TEventInterface):
        raise NotImplementedError
