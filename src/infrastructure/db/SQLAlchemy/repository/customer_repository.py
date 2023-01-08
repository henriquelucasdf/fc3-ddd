from typing import List
from sqlalchemy.orm import Session

from src.domain.entity.address import Address
from src.domain.entity.customer import Customer

from src.infrastructure.db.SQLAlchemy.model.customer_model import CustomerModel
from src.domain.customer.repository.customer_repository_interface import CustomerRepositoryInterface


class CustomerRepository(CustomerRepositoryInterface):

    def __init__(self, session: Session):
        self.session = session

    def create(self, entity: Customer) -> None:
        customer_model = CustomerModel(
            id=entity.get_id(),
            name=entity.get_name(),
            street=entity._address.street,
            number=entity._address.number,
            zip=entity._address.zip,
            city=entity._address.city,
            active=entity.is_active(),
            reward_points=entity.get_reward_points()
        )

        self.session.add(customer_model)
        self.session.commit()

    def update(self, entity: Customer) -> None:
        customer_model = CustomerModel(
            id=entity.get_id(),
            name=entity.get_name(),
            street=entity._address.street,
            number=entity._address.number,
            zip=entity._address.zip,
            city=entity._address.city,
            active=entity.is_active(),
            reward_points=entity.get_reward_points()
        )

        self.session.query(CustomerModel).filter_by(id=customer_model.id).update({
            "name": customer_model.name,
            "street": customer_model.street,
            "number": customer_model.number,
            "zip": customer_model.zip,
            "city": customer_model.city,
            "active": customer_model.active,
            "reward_points": customer_model.reward_points,
        })

        self.session.commit()

    def find(self, id: str) -> Customer:
        cm = self.session.query(
            CustomerModel).filter_by(id=id).first()

        if cm is None:
            raise ValueError("Customer Not Found")

        return self._build_customer_entity(cm)

    def find_all(self) -> List[Customer]:
        models_list = self.session.query(CustomerModel).all()
        return [self._build_customer_entity(model) for model in models_list]

    @staticmethod
    def _build_customer_entity(model: CustomerModel) -> Customer:
        address = Address(
            street=model.street,
            number=model.number,
            zip=model.zip,
            city=model.city
        )

        customer_entity = Customer(
            id=model.id,
            name=model.name,
            address=address,
            active=model.active
        )
        customer_entity._rewardPoints = model.reward_points

        return customer_entity
