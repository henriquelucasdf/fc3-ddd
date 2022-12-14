import pytest
from src.domain.customer.entity.customer import Customer
from src.domain.customer.entity.address import Address


def test_show_throw_error_when_id_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Customer("", "John")

    assert str(error_info.value) == "Id is required"


def test_show_throw_error_when_name_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Customer("123", "")

    assert str(error_info.value) == "Name is required"


def test_should_change_name():
    customer = Customer("123", "John")
    customer.change_name("Jane")

    assert customer.get_name() == "Jane"


def test_should_activate_customer():
    customer = Customer("123", "John")
    address = Address(
        street="Street 1",
        number=123,
        zip="1234567",
        city="Any"
    )

    customer.set_address(address)
    customer.activate()

    assert customer.is_active()


def test_should_deactivate_customer():
    customer = Customer("123", "John")
    address = Address(
        street="Street 1",
        number=123,
        zip="1234567",
        city="Any"
    )

    customer.set_address(address)
    customer.activate()

    if customer.is_active():
        customer.deactivate()
        assert not customer.is_active()
    else:
        raise ValueError("Not activated")


def test_activate_should_throw_error_without_address():
    customer = Customer("123", "John")

    with pytest.raises(ValueError) as error_info:
        customer.activate()

    assert str(error_info.value) == "Address is mandatory to activate a customer"


def test_reward_points_should_be_zero_when_initialized():
    customer = Customer("123", "John")
    assert customer.get_reward_points() == 0


def test_should_add_reward_points():
    customer = Customer("123", "John")
    customer.add_reward_points(12)
    customer.add_reward_points(13)

    assert customer.get_reward_points() == 25
