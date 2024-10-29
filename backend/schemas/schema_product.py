# schemas/schema_product.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    description: str
    category: str
    price: float
    compare_at_price: float | None = None
    cost_per_item: float | None = None
    margin: float | None = None
    inventory_quantity: int
    sku: str | None = None
    barcode: str | None = None
    status: str
    product_type: str
    vendor: str | None = None
    tags: str | None = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
