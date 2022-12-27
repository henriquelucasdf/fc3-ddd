from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.domain.entity.product import Product

from src.domain.repository.product_repository_interface import ProductRepositoryInterface
from src.infrastructure.db.SQLAlchemy.model.product_model import ProductModel, BaseModel

engine = create_engine('sqlite://')
Session = sessionmaker(bind=engine)


class TestProduct:
    def setup_class(self):
        BaseModel.metadata.create_all(engine)

        self.session = Session()
        self.valid_product = ProductModel(
            id="789",
            name="product_test",
            price=10)

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_product_valid(self):
        self.session.add(self.valid_product)
        self.session.commit()

        valid_product = self.session.query(
            ProductModel).filter_by(name="product_test").first()

        assert valid_product.name == "product_test"
        assert valid_product.id == "789"
        assert valid_product.price == 10

    # def test_should_create_a_product(self):
    #     product_repository = ProductRepository()
    #     product = Product("1", "product 1", 100)

    #     # insert data using the repository
    #     product_repository.create(product)
