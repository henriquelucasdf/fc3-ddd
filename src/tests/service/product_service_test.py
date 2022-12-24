from src.domain.entity.product import Product
from src.domain.service.product_service import ProductService


def test_should_change_price_of_all_products():
    product_1 = Product("id1", "name1", 10)
    product_2 = Product("id2", "name2", 20)
    products = [product_1, product_2]

    ProductService.increase_price(products, 100)

    assert product_1.get_price() == 20
    assert product_2.get_price() == 40
