from uuid import uuid4
from src.domain.customer.entity.address import Address
from src.domain.customer.entity.customer import Customer


class CustomerFactory:

    @staticmethod
    def create(name: str) -> Customer:
        return Customer(str(uuid4()), name)

    @staticmethod
    def create_with_address(name: str, address: Address) -> Customer:
        customer = Customer(str(uuid4), name)
        customer.set_address(address)
        return customer
