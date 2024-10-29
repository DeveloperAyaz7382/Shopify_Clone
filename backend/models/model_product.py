# models.py
from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String)
    price = Column(Float)
    compare_at_price = Column(Float, nullable=True)
    cost_per_item = Column(Float, nullable=True)
    margin = Column(Float, nullable=True)
    inventory_quantity = Column(Integer, default=0)
    sku = Column(String, unique=True, nullable=True)
    barcode = Column(String, nullable=True)
    status = Column(String, default="active")
    product_type = Column(String)
    vendor = Column(String, nullable=True)
    tags = Column(String, nullable=True)
