from dataclasses import dataclass
from typing import List, TypedDict

from src.domain.order.entity.order import Order
from src.domain.order.entity.order_item import OrderItem


class ItemsArgsInterface(TypedDict):
    id: str
    name: str
    product_id: str
    quantity: int
    price: float


@dataclass
class OrderArgsInterface:
    id: str
    customer_id: str
    items: List[ItemsArgsInterface]


class OrderFactory:

    @staticmethod
    def create(order_args: dict) -> Order:
        _order_args = OrderArgsInterface(**order_args)
        order_items = [OrderItem(**_item)
                       for _item in _order_args.items]

        return Order(
            id=_order_args.id,
            customerId=_order_args.customer_id,
            items=order_items
        )
