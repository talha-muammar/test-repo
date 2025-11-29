from pydantic import BaseModel, EmailStr
from .address import AddressResponse, AddressBase


class BuyerBase(BaseModel):
    name: str
    phone: str
    email: EmailStr


class BuyerCreate(BuyerBase):
    password: str


class BuyerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: AddressBase | None = None


class BuyerResponse(BuyerBase):
    user_id: int
    total_spent: float
    address: AddressResponse | None

    class Config:
        orm_mode = True
