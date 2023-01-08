from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Float
from src.infrastructure.shared.repository.SQLAlchemy.base_model import BaseModel
from src.infrastructure.order.repository.SQLAlchemy.order_item_model import OrderItemModel


class OrderModel(BaseModel):
    __tablename__ = "order"

    id = Column(String(50), primary_key=True)
    customer_id = Column(String(50), ForeignKey(
        'customer.id', ondelete="CASCADE"), nullable=False)
    total = Column(Float, nullable=False)

    # Relationships
    items = relationship("OrderItemModel", backref="order", post_update=True)
