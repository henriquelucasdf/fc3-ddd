import logging
from src.domain.event.product.product_created_event import ProductCreatedEvent
from src.domain.event.shared.event_handler_interface import EventHandlerInterface

logger = logging.getLogger("__main__")


class SendEmailWhenProductIsCreatedHandler(EventHandlerInterface[ProductCreatedEvent]):

    def handle(self, event: ProductCreatedEvent) -> None:
        logger.info(f"Sending email to {event.event_data.get('email')}")
