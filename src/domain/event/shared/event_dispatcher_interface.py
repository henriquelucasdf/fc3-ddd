from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from src.domain.event.shared.event_interface import EventInterface
from src.domain.event.shared.event_handler_interface import EventHandlerInterface

TEventInterface = TypeVar("TEventInterface", bound="EventInterface")
TEventHandlerInterface = TypeVar(
    "TEventHandlerInterface", bound="EventHandlerInterface")


class EventDispatcherInterface(ABC, Generic[TEventInterface]):

    @abstractmethod
    def notify(self, event: TEventInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def register(self, event_name: str, event_handler: TEventHandlerInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister(self, event_name: str, event_handler: TEventHandlerInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister_all(self) -> None:
        raise NotImplementedError
