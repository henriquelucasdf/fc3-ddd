from typing import List

from src.domain.entity.product import Product


class ProductService:

    @staticmethod
    def increase_price(products: List[Product], percentage: float) -> None:
        for product_ in products:
            new_price = product_.get_price() * (1 + percentage/100)
            product_.change_price(new_price)
