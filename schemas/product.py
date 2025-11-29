from pydantic import BaseModel
from datetime import datetime
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image_url: str


class ProductCreate(ProductBase):
    category_id: int
    inventory_id: int | None = None


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    image_url: str | None = None
    category_id: int | None = None


class ProductResponse(ProductBase):
    product_id: int
    date_added: datetime
    is_available: bool
    category: CategoryResponse | None

    class Config:
        orm_mode = True
