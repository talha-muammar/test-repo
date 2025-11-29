from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class Buyer(Base):
    __tablename__ = "buyers"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    password_hash = Column(String)
    total_spent = Column(Float, default=0.0)


    address_id = Column(Integer, ForeignKey("addresses.id"), unique=True)
    address = relationship("Address")
