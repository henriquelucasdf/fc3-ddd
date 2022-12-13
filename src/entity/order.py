from typing import List
from entity.order_item import OrderItem


class Order:
    def __init__(
        self,
        _id: str,
        _customerId: str,
        _items: List[OrderItem] = []
    ) -> None:

        self._id = _id
        self._customerId = _customerId
        self._items = _items

    def total(self) -> float:
        return sum([item._price for item in self._items])
