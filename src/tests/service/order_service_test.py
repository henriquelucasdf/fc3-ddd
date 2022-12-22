import pytest
from src.entity.order import Order
from src.entity.order_item import OrderItem
from src.service.order_service import OrderService


def test_should_get_total_of_all_orders():
    item1 = OrderItem("i1", "item1", 100, "p1", 1)
    item2 = OrderItem("i2", "item2", 200, "p2", 2)

    order1 = Order("o1", "c1", [item1])
    order2 = Order("o2", "c2", items=[item2])

    total = OrderService.total_price([order1, order2])
    assert total == 500
