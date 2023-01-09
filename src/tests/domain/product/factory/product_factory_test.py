from src.domain.product.factory.product_factory import ProductFactory


def test_should_create_a_product():
    product = ProductFactory.create("Product A", 1)

    assert product.get_id() is not None
    assert product.get_name() == "Product A"
    assert product.get_price() == 1
    assert product.__class__.__name__ == "Product"
