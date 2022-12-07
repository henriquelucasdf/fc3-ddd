from typing import Optional
from address import Address


class Customer:
    def __init__(
        self,
        _id: str,
        _name: str,
        _address: Optional[Address] = None,
        _active: Optional[bool] = False
    ) -> None:
        self._id = _id
        self._name = _name
        self._address = _address
        self._active = _active

        self.validate()

    def validate(self) -> None:
        if not len(self._name):
            raise ValueError("Name is required")

        if not len(self._id):
            raise ValueError("Id is required")

    def change_name(self, name: str) -> None:
        self._name = name
        self.validate()

    def activate(self) -> None:
        if self._address is None:
            raise ValueError("Address is mandatory to activate a customer")

        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def set_address(self, address: Address) -> None:
        self._address = address
