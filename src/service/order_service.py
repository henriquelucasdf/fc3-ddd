import uuid
from typing import List
from src.entity.customer import Customer
from src.entity.order import Order
from src.entity.order_item import OrderItem


class OrderService:

    @staticmethod
    def total_price(orders_list: List) -> float:
        return sum(order_.get_total() for order_ in orders_list)

    @staticmethod
    def place_order(customer: Customer, items: List[OrderItem]) -> Order:

        if not len(items):
            raise ValueError("Order must have at least one item.")

        new_order = Order(str(uuid.uuid4()), customer.get_id(), items)

        # reward points = price of order / 2
        customer.add_reward_points(new_order.get_total()/2)

        return new_order
