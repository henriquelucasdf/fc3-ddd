import pytest
from src.domain.entity.order import Order
from src.domain.entity.order_item import OrderItem


def test_should_throw_error_when_id_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Order(
            id="",
            customerId="123",
            items=[]
        )
    assert str(error_info.value) == "Id is required"


def test_should_throw_error_when_customerId_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Order(
            id="123",
            customerId="",
            items=[]
        )
    assert str(error_info.value) == "customerId is required"


def test_should_throw_error_when_items_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Order(
            id="123",
            customerId="456",
            items=[]
        )
    assert str(error_info.value) == "items quantity must be greater than zero"


def test_should_calculate_total():
    mock_items = [
        OrderItem(f"item{i}", f"name{i}", i, f"p{i}", i) for i in range(1, 4)]
    order_class = _ = Order(
        id="123",
        customerId="456",
        items=mock_items
    )

    assert order_class.total() == 14
