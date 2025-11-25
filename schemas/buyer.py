from pydantic import BaseModel
from schemas.address import AddressBase
from schemas.address import AddressOut

class BuyerCreate(BaseModel):
    name: str
    email: str
    phone: str
    password: str
    address: AddressBase

class BuyerOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    created_at: str
    address: AddressOut

    class Config:
        orm_mode = True