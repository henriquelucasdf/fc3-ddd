from src.domain.event.product.handler.send_email_when_product_is_created_handler import SendEmailWhenProductIsCreatedHandler
from src.domain.event.shared.event_dispatcher import EventDispatcher


def test_should_register_an_event_handler():
    event_dispatcher = EventDispatcher()
    event_handler = SendEmailWhenProductIsCreatedHandler()

    event_dispatcher.register("ProductCreatedEvent", event_handler)

    # assertion
    registered_handlers = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler in registered_handlers
    assert len(registered_handlers) == 1
