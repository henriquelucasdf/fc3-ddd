from src.domain.customer.entity.address import Address
from src.domain.customer.factory.customer_factory import CustomerFactory


def test_should_create_a_customer():
    customer = CustomerFactory.create("John")

    assert customer.get_id() is not None
    assert customer.get_name() == "John"
    assert customer.get_address() is None


def test_should_create_a_customer_with_an_address():
    address = Address(street="123 Street", number=1, zip="123456", city="SP")
    customer = CustomerFactory.create_with_address("John", address)

    assert customer.get_id() is not None
    assert customer.get_name() == "John"
    assert customer.get_address() == address
