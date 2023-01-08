import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.domain.order.entity.order import Order
from src.domain.order.entity.order_item import OrderItem
from src.domain.customer.entity.address import Address
from src.domain.customer.entity.customer import Customer
from src.domain.product.entity.product import Product
from src.infrastructure.shared.repository.SQLAlchemy.base_model import BaseModel
from src.infrastructure.order.repository.SQLAlchemy.order_model import OrderModel
from src.infrastructure.order.repository.SQLAlchemy.order_repository import OrderRepository
from src.infrastructure.product.repository.SQLAlchemy.product_repository import ProductRepository
from src.infrastructure.customer.repository.SQLAlchemy.customer_repository import CustomerRepository


engine = create_engine('sqlite://')
Session = sessionmaker(bind=engine)


class TestOrder:
    def setup_class(self):
        BaseModel.metadata.create_all(engine)
        self.session = Session()

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_should_create_a_new_order(self):
        # create a customer
        address = Address(
            street="street 1",
            number=1,
            zip="1111111",
            city="City 1"
        )
        customer = Customer(
            id="C1",
            name="Customer test 1",
            address=address,
            active=True
        )

        customer_repository = CustomerRepository(self.session)
        customer_repository.create(customer)

        # create a product
        product = Product("P1", "Product 1", 10)
        product_repository = ProductRepository(self.session)
        product_repository.create(product)

        # Creating an Order
        # create a item
        order_item1 = OrderItem(
            "OI1",
            product.get_name(),
            product.get_price(),
            product._id,
            2
        )

        order_item2 = OrderItem(
            "OI2",
            product.get_name(),
            product.get_price(),
            product._id,
            4
        )

        # create an Order Entity
        order = Order("O1", customer.get_id(), [order_item1, order_item2])

        # Create using the Repository
        order_repository = OrderRepository(self.session)
        order_repository.create(order)

        # retrieving for assertion
        query_order = self.session.query(OrderModel).filter_by(id="O1").first()
        query_items_list = query_order.items

        assert query_order.customer_id == "C1"
        assert query_order.total == 60
        assert query_items_list[0].id == "OI1"
        assert query_items_list[1].id == "OI2"
        assert query_items_list[0].product_id == "P1"
        assert query_items_list[0].order_id == "O1"
        assert query_items_list[0].name == "Product 1"
