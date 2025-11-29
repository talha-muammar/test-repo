from pydantic import BaseModel, EmailStr
from enum import Enum

class AdminBase(BaseModel):
    name: str
    phone: str
    email: EmailStr

class AdminCreate(AdminBase):
    password: str


class AdminUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None


class AdminResponse(AdminBase):
    admin_id: int
    total_revenue: float

    class Config:
        orm_mode = True
