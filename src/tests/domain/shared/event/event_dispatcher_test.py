from datetime import datetime
from unittest.mock import patch
from src.domain.shared.event.event_dispatcher import EventDispatcher
from src.domain.product.event.product_created_event import ProductCreatedEvent
from src.domain.product.event.handler.send_email_when_product_is_created_handler import (
    SendEmailWhenProductIsCreatedHandler)

HANDLER_PATH = "src.domain.product.event.handler"


def test_should_register_an_event_handler():
    event_dispatcher = EventDispatcher()
    event_handler = SendEmailWhenProductIsCreatedHandler()

    event_dispatcher.register("ProductCreatedEvent", event_handler)

    # assertion
    registered_handlers = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler in registered_handlers
    assert len(registered_handlers) == 1


def test_should_unregister_an_event_handler():
    event_dispatcher = EventDispatcher()
    event_handler = SendEmailWhenProductIsCreatedHandler()

    event_dispatcher.register("ProductCreatedEvent", event_handler)

    registered_handlers = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler in registered_handlers

    event_dispatcher.unregister("ProductCreatedEvent", event_handler)

    registered_handlers2 = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler not in registered_handlers2
    assert len(registered_handlers2) == 0


def test_should_unregister_all_event_handlers():
    event_dispatcher = EventDispatcher()
    event_handler = SendEmailWhenProductIsCreatedHandler()

    event_dispatcher.register("ProductCreatedEvent", event_handler)

    registered_handlers = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler in registered_handlers

    event_dispatcher.unregister_all()

    registered_handlers2 = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert registered_handlers2 is None


@patch(f"{HANDLER_PATH}.send_email_when_product_is_created_handler.SendEmailWhenProductIsCreatedHandler.handle")
def test_should_notify_all_event_handlers(mock_handle):
    event_dispatcher = EventDispatcher()
    event_handler = SendEmailWhenProductIsCreatedHandler()
    product_created_event = ProductCreatedEvent(
        datetime_ocurred=datetime.now(),
        event_data={
            "name": "Product 1",
            "description": "Product 1 description.",
            "price": 10
        }
    )

    event_dispatcher.register("ProductCreatedEvent", event_handler)

    registered_handlers = event_dispatcher.get_event_handlers(
        "ProductCreatedEvent")

    assert event_handler in registered_handlers

    event_dispatcher.notify(event=product_created_event)
    mock_handle.assert_called_once()
