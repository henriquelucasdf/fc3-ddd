from typing import List
from sqlalchemy.orm import Session

from src.domain.entity.order import Order
from src.domain.entity.order_item import OrderItem

from src.infrastructure.db.SQLAlchemy.model.order_model import OrderModel
from src.infrastructure.db.SQLAlchemy.model.order_item_model import OrderItemModel
from src.domain.repository.order_repository_interface import OrderRepositoryInterface


class OrderRepository(OrderRepositoryInterface):

    def __init__(self, session: Session):
        self.session = session

    def create(self, entity: Order) -> None:
        new_order_model = self._entity_to_model(entity)

        self.session.add(new_order_model)
        self.session.commit()

    def update(self, entity: Order) -> None:
        old_order_model = self.session.query(
            OrderModel).filter_by(id=entity._id).first()
        new_order_model = self._entity_to_model(entity)

        self._update_order_items(new_order_model.items)

    def find(self, id: str) -> Order:
        pass

    def find_all(self) -> List[Order]:
        pass

    @staticmethod
    def _entity_to_model(entity: Order) -> OrderModel:
        model = OrderModel(
            id=entity._id,
            customer_id=entity._customerId,
            total=entity.get_total(),
            items=[
                OrderItemModel(
                    id=item._id,
                    product_id=item._product_id,
                    order_id=entity._id,
                    name=item._name,
                    quantity=item._quantity,
                    price=item._price
                ) for item in entity._items
            ]
        )

        return model
