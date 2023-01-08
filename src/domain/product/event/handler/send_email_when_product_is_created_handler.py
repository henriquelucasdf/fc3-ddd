import logging
from src.domain.product.event.product_created_event import ProductCreatedEvent
from src.domain.shared.event.event_handler_interface import EventHandlerInterface

logger = logging.getLogger("__main__")


class SendEmailWhenProductIsCreatedHandler(EventHandlerInterface[ProductCreatedEvent]):

    def handle(self, event: ProductCreatedEvent) -> None:
        logger.info("Sending email to ...")
