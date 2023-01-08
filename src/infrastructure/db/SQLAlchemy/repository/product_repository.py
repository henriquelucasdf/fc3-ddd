from typing import List
from src.domain.product.entity.product import Product
from src.domain.product.repository.product_repository_interface import ProductRepositoryInterface
from src.infrastructure.db.SQLAlchemy.model.product_model import ProductModel
from sqlalchemy.orm import Session


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, entity: Product) -> None:

        model = ProductModel(
            id=entity._id,
            name=entity._name,
            price=entity._price
        )
        self.session.add(model)
        self.session.commit()

    def update(self, entity: Product) -> None:
        model = ProductModel(
            id=entity._id,
            name=entity._name,
            price=entity._price
        )
        self.session.query(ProductModel).filter_by(id=entity._id).update({
            "name": model.name,
            "price": model.price
        })
        self.session.commit()

    def find(self, id: str) -> Product:
        product_model = self.session.query(
            ProductModel).filter_by(id=id).first()

        return Product(
            id=product_model.id,
            name=product_model.name,
            price=product_model.price
        )

    def find_all(self) -> List[Product]:
        models_list = self.session.query(ProductModel).all()

        return [Product(model.id, model.name, model.price) for model in models_list]
