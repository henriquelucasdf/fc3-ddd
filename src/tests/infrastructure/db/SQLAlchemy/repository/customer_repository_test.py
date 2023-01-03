import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.domain.entity.address import Address
from src.domain.entity.customer import Customer
from src.infrastructure.db.SQLAlchemy.model.customer_model import CustomerModel, BaseModel
from src.infrastructure.db.SQLAlchemy.repository.customer_repository import CustomerRepository


engine = create_engine('sqlite://')
Session = sessionmaker(bind=engine)


class TestCustomer:
    def setup_class(self):
        BaseModel.metadata.create_all(engine)

        self.session = Session()
        self.valid_customer = CustomerModel(
            id="C0",
            name="valid customer",
            active=True,
            street="1234 Street",
            number=4,
            zip="1233456",
            city="Test city",
            reward_points=0.0
        )

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_customer_valid(self):
        self.session.add(self.valid_customer)
        self.session.commit()

        query_customer = self.session.query(
            CustomerModel).filter_by(id="C0").first()

        assert query_customer.name == "valid customer"
        assert query_customer.street == "1234 Street"
        assert query_customer.number == 4
        assert query_customer.zip == "1233456"

    def test_should_create_customer(self):
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

        # creating
        customer_repository = CustomerRepository(self.session)
        customer_repository.create(customer)

        # retrieving for assertion
        query_customer = self.session.query(
            CustomerModel).filter_by(id="C1").first()

        assert query_customer.name == "Customer test 1"
        assert query_customer.number == 1
        assert query_customer.zip == "1111111"
        assert query_customer.street == "street 1"

    def test_should_update_customer(self):
        customer_to_update = self.session.query(
            CustomerModel).filter_by(id="C1").first()

        address_vo = Address(
            street=customer_to_update.street,
            number=customer_to_update.number,
            zip=customer_to_update.zip,
            city=customer_to_update.city
        )

        customer_entity = Customer(
            id=customer_to_update.id,
            name=customer_to_update.name,
            active=customer_to_update.active,
            address=address_vo
        )

        customer_entity._rewardPoints = customer_to_update.reward_points

        # updates
        customer_entity.add_reward_points(10)
        customer_entity.change_name("Customer test 2")

        # update in DB
        customer_repository = CustomerRepository(self.session)
        customer_repository.update(customer_entity)

        # query for assertion
        customer_query = self.session.query(
            CustomerModel).filter_by(id="C1").first()

        assert customer_query.name == "Customer test 2"
        assert customer_query.reward_points == 10

    def test_should_find_a_customer(self):

        # create new customer
        address = Address(
            street="street 2",
            number=2,
            zip="222222",
            city="City 2"
        )
        customer = Customer(
            id="C2",
            name="Customer test 2",
            address=address,
            active=True
        )
        customer.add_reward_points(2)

        # add to DB
        customer_repository = CustomerRepository(self.session)
        customer_repository.create(customer)

        # search customer
        found_customer = customer_repository.find(id="C2")

        assert found_customer.get_name() == "Customer test 2"
        assert found_customer._address.street == "street 2"
        assert found_customer._address.city == "City 2"
        assert found_customer.get_reward_points() == 2

    def test_find_should_throw_an_error(self):
        customer_repository = CustomerRepository(self.session)
        with pytest.raises(ValueError) as error_info:
            _ = customer_repository.find(id="ASDASD")

        assert str(error_info.value) == "Customer Not Found"

    def test_should_find_all_customers(self):
        customer_repository = CustomerRepository(self.session)
        customers_list = customer_repository.find_all()
        ids_list = [customer.get_id() for customer in customers_list]

        assert not len(set(["C0", "C1", "C2"]) - set(ids_list))
