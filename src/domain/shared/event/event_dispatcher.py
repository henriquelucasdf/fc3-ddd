from typing import Dict, List, Optional
from src.domain.shared.event.event_dispatcher_interface import (
    EventDispatcherInterface)
from src.domain.shared.event.event_interface import EventInterface
from src.domain.shared.event.event_handler_interface import EventHandlerInterface


class EventDispatcher(EventDispatcherInterface):

    def __init__(self) -> None:
        self.event_handlers: Dict[str, List[EventHandlerInterface]] = {}

    def notify(self, event: EventInterface) -> None:
        event_name = event.__class__.__name__
        handlers = self.event_handlers.get(event_name)

        if isinstance(handlers, list):
            for handler in handlers:
                handler.handle(event)

        else:
            raise ValueError(f"Handler for event {event_name} was not found")

    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if self.event_handlers.get(event_name) is None:
            self.event_handlers[event_name] = []

        self.event_handlers[event_name].append(event_handler)

    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if self.event_handlers.get(event_name) is None:
            raise ValueError(f"Event name {event_name} is not registered")

        try:
            self.event_handlers[event_name].remove(event_handler)

        except ValueError as e:
            raise e

    def unregister_all(self) -> None:
        self.event_handlers = {}

    def get_event_handlers(self, event_name: str) -> Optional[List[EventHandlerInterface]]:
        return self.event_handlers.get(event_name)
