from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from src.infrastructure.shared.repository.SQLAlchemy.base_model import BaseModel
from src.infrastructure.product.repository.SQLAlchemy.product_model import ProductModel


class OrderItemModel(BaseModel):
    __tablename__ = "order_items"

    id = Column(String(50), primary_key=True)
    product_id = Column(String(50), ForeignKey(
        'product.id'), nullable=False)
    order_id = Column(String(50), ForeignKey(
        'order.id'), nullable=False)
    name = Column(String(250), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # relashionships
    products = relationship("ProductModel", post_update=True)
