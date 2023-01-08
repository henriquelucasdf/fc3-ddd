from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float, Boolean, Integer
from src.infrastructure.order.repository.SQLAlchemy.order_model import OrderModel
from src.infrastructure.shared.repository.SQLAlchemy.base_model import BaseModel


class CustomerModel(BaseModel):
    __tablename__ = "customer"

    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    street = Column(String(250), nullable=False)
    number = Column(Integer, nullable=False)
    zip = Column(String(50), primary_key=True)
    city = Column(String(250), nullable=False)
    active = Column(Boolean, nullable=False)
    reward_points = Column(Float, nullable=False)

    # Address is a value object in the domain
    # But in the DB, it's just a column
    # We need to model the DB based in the domain, not the inverse

    # relationships
    orders = relationship("OrderModel", backref="customer", post_update=True)
