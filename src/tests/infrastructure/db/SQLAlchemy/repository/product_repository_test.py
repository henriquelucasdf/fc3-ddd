from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.domain.product.entity.product import Product
from src.infrastructure.db.SQLAlchemy.model.base_model import BaseModel
from src.infrastructure.db.SQLAlchemy.model.product_model import ProductModel
from src.infrastructure.db.SQLAlchemy.repository.product_repository import ProductRepository

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

    def test_should_create_a_product(self):
        product_repository = ProductRepository(self.session)
        product = Product("1", "product_1", 100)

        # insert data using the repository
        product_repository.create(product)

        product_test = self.session.query(
            ProductModel).filter_by(name="product_1").first()

        assert product_test.name == "product_1"
        assert product_test.id == "1"
        assert product_test.price == 100

    def test_should_update_a_product(self):
        product_repository = ProductRepository(self.session)
        product_to_update = self.session.query(
            ProductModel).filter_by(id="1").first()

        product = Product(
            id=product_to_update.id,
            name=product_to_update.name,
            price=product_to_update.price
        )

        product.change_name("product_2")
        product.change_price(500)

        # insert data using the repository
        product_repository.update(product)

        product_query = self.session.query(
            ProductModel).filter_by(id="1").first()

        assert product_query.id == "1"
        assert product_query.name == "product_2"
        assert product_query.price == 500

    def test_should_find_a_product(self):
        product_repository = ProductRepository(self.session)
        product = Product("3", "product_3", 300)

        product_repository.create(product)

        found_product = product_repository.find(id="3")
        assert found_product.get_name() == "product_3"
        assert found_product.get_price() == 300

    def test_should_find_all_products(self):
        product_repository = ProductRepository(self.session)

        products_list = product_repository.find_all()
        ids_list = [prod._id for prod in products_list]

        assert not len(set(["1", "3", "789"]) - set(ids_list))
