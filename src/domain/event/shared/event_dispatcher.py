from typing import Dict, List
from src.domain.event.shared.event_dispatcher_interface import (
    EventDispatcherInterface, TEventHandlerInterface, TEventInterface)


class EventDispatcher(EventDispatcherInterface):

    def __init__(self) -> None:
        self.event_handlers: Dict[str, List[TEventHandlerInterface]] = {}

    def notify(self, event: TEventInterface) -> None:
        raise NotImplementedError

    def register(self, event_name: str, event_handler: TEventHandlerInterface) -> None:
        if self.event_handlers.get(event_name) is None:
            self.event_handlers[event_name] = []

        self.event_handlers[event_name].append(event_handler)

    def unregister(self, event_name: str, event_handler: TEventHandlerInterface) -> None:
        raise NotImplementedError

    def unregister_all(self) -> None:
        raise NotImplementedError

    def get_event_handlers(self, event_name: str) -> List[TEventHandlerInterface]:
        return self.event_handlers.get(event_name)
