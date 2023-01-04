from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float
from src.infrastructure.db.SQLAlchemy.model.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = "product"

    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
