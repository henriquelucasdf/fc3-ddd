from typing import List
from src.entity.order import Order


class OrderService:

    @staticmethod
    def total_price(orders_list: List) -> float:
        return sum(order_.get_total() for order_ in orders_list)
