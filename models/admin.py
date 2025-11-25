from sqlalchemy import Column, Integer, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

from db.database import Base

class AccessLevel(enum.Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    access_level = Column(Enum(AccessLevel), default=AccessLevel.Low)
    total_revenue = Column(Float, default=0.0)
