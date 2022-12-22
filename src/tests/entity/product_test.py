import pytest
from src.entity.product import Product


def test_product_should_throw_error_when_id_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Product(
            id="",
            name="123",
            price=100
        )
    assert str(error_info.value) == "Id is required"


def test_product_should_throw_error_when_name_is_empty():
    with pytest.raises(ValueError) as error_info:
        _ = Product(
            id="123",
            name="",
            price=100
        )
    assert str(error_info.value) == "Name is required"


def test_product_should_throw_error_when_price_is_negative():
    with pytest.raises(ValueError) as error_info:
        _ = Product(
            id="123",
            name="456",
            price=-1
        )
    assert str(error_info.value) == "Price must be greater than zero"


def test_change_name_must_modify_atribute_name():
    or_class = Product("123", "name1", 100)
    or_class.change_name(new_name="name2")

    assert or_class.get_name() == "name2"


def test_changeprice_must_modify_atribute_price():
    or_class = Product("123", "name1", 100)
    or_class.change_price(new_price=200)

    assert or_class.get_price() == 200
