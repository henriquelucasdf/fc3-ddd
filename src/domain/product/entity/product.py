from src.domain.product.entity.product_interface import ProductInterface


class Product(ProductInterface):
    def __init__(
        self,
        id: str,
        name: str,
        price: float
    ) -> None:

        self._id = id
        self._name = name
        self._price = price

        self.validate()

    def validate(self) -> None:
        if not len(self._id):
            raise ValueError("Id is required")

        if not len(self._name):
            raise ValueError("Name is required")

        if self._price < 0:
            raise ValueError("Price must be greater than zero")

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def change_name(self, new_name: str) -> None:
        self._name = new_name

    def change_price(self, new_price: float) -> None:
        self._price = new_price
