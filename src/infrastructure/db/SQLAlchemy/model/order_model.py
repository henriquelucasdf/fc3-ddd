from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Float
from src.infrastructure.db.SQLAlchemy.model.base_model import BaseModel


class OrderModel(BaseModel):
    __tablename__ = "order"

    id = Column(String(50), primary_key=True)
    customer_id = Column(String(50), ForeignKey(
        'customer.id', ondelete="CASCADE"), nullable=False)
    total = Column(Float, nullable=False)

    # Relationships
    customer = relationship("CustomerModel", back_populates="orders")
    items = relationship("OrderItemModel", back_populates="order")
