from abc import ABC, abstractmethod


class ProductInterface (ABC):
    def __init__(
        self,
        id: str,
        name: str,
        price: float
    ) -> None:

        self._id = id
        self._name = name
        self._price = price

    @abstractmethod
    def get_id(self) -> str:
        return self._id

    @abstractmethod
    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_price(self) -> float:
        return self._price
