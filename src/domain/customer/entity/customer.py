from typing import Optional
from src.domain.customer.entity.address import Address


class Customer:
    def __init__(
        self,
        id: str,
        name: str,
        address: Optional[Address] = None,
        active: Optional[bool] = False
    ) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._active = active
        self._rewardPoints = 0.0

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

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> str:
        return self._id

    def get_address(self) -> Optional[Address]:
        return self._address

    def is_active(self) -> Optional[bool]:
        return self._active

    def add_reward_points(self, points: float) -> None:
        self._rewardPoints += points

    def get_reward_points(self) -> float:
        return self._rewardPoints
