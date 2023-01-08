from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from src.domain.shared.event.event_interface import EventInterface
from src.domain.shared.event.event_handler_interface import EventHandlerInterface


class EventDispatcherInterface(ABC):

    @abstractmethod
    def notify(self, event: EventInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister_all(self) -> None:
        raise NotImplementedError
