from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from src.infrastructure.db.SQLAlchemy.model.base_model import BaseModel
from src.infrastructure.db.SQLAlchemy.model.product_model import ProductModel


class OrderItemModel(BaseModel):
    __tablename__ = "order_items"

    id = Column(String(50), primary_key=True)
    product_id = Column(String(50), ForeignKey(
        'product.id', ondelete="CASCADE"), nullable=False)
    order_id = Column(String(50), ForeignKey(
        'order.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(250), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # relashionships
    products = relationship("ProductModel")
