import pytest
from src.domain.customer.entity.address import Address


@pytest.mark.parametrize(
    "street_param, zip_param, city_param",
    [
        ("", "123", "asdf"),
        ("123", "", "asdf"),
        ("123", "456", "")
    ]
)
def test_empty_inputs_must_throw_error(
    street_param,
    zip_param,
    city_param
):
    with pytest.raises(ValueError):
        _ = Address(
            street=street_param,
            number=123,
            zip=zip_param,
            city=city_param
        )
