class OrderItem:
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        product_id: str,
        quantity: int
    ) -> None:

        self._id = id
        self._name = name
        self._price = price
        self._product_id = product_id
        self._quantity = quantity

        self.validate()

    def validate(self) -> None:
        if self._quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
