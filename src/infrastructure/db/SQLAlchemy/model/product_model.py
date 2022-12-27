from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float

BaseModel = declarative_base()


class ProductModel(BaseModel):
    __tablename__ = "product"

    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
