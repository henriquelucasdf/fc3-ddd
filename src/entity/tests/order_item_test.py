import pytest
from src.entity.order_item import OrderItem


def test_should_throw_error_if_qtd_is_zero_or_less():
    with pytest.raises(ValueError) as err_info:
        _ = OrderItem("123", "name", 200, "123", -1)

    assert str(err_info.value) == "Quantity must be greater than zero"
