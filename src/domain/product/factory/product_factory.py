from uuid import uuid4
from src.domain.product.entity.product import Product
from src.domain.product.entity.product_interface import ProductInterface


class ProductFactory:

    @staticmethod
    def create(name: str, price: float) -> ProductInterface:
        return Product(str(uuid4()), name, price)
