from pydantic import BaseModel


class AddressBase(BaseModel):
    house_no: int
    street: str
    city: str
    postal_code: str


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True
