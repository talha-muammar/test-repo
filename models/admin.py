from sqlalchemy import Column, Integer, Float, Enum, String
from sqlalchemy.orm import relationship
import enum
from db.database import Base


class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    password_hash = Column(String)
