import pytest
from src.domain.entity.order import Order
from src.domain.entity.customer import Customer
from src.domain.entity.order_item import OrderItem
from src.domain.service.order_service import OrderService


def test_should_get_total_of_all_orders():
    item1 = OrderItem("i1", "item1", 100, "p1", 1)
    item2 = OrderItem("i2", "item2", 200, "p2", 2)

    order1 = Order("o1", "c1", [item1])
    order2 = Order("o2", "c2", items=[item2])

    total = OrderService.total_price([order1, order2])
    assert total == 500


def test_should_place_an_order():
    customer = Customer("c1", "name1", "add1", True)
    item1 = OrderItem("it1", "item1", 10, "p1", 1)

    order = OrderService.place_order(customer, [item1])

    assert customer.get_reward_points() == 5
    assert order.get_total() == 10


def test_should_raise_an_error():
    customer = Customer("c1", "name1", "add1", True)
    with pytest.raises(ValueError):
        OrderService.place_order(customer, [])
