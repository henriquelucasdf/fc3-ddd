from typing import List
from entity.order_item import OrderItem


class Order:
    def __init__(
        self,
        id: str,
        customerId: str,
        items: List[OrderItem] = []
    ) -> None:

        self._id = id
        self._customerId = customerId
        self._items = items
        self._total = self.total()

        self.validate()

    def total(self) -> float:
        return sum([item._price * item._quantity for item in self._items])

    def validate(self) -> None:
        if not len(self._id):
            raise ValueError("Id is required")

        if not len(self._customerId):
            raise ValueError("customerId is required")

        if not len(self._items):
            raise ValueError("items quantity must be greater than zero")
