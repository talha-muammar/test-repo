from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)

    # Former user.py attributes
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Buyer-specific field
    address_id = Column(Integer, ForeignKey("addresses.id"), unique=True)
    address = relationship("Address")
