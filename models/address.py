from sqlalchemy import Column, Integer, String
from db.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    house_no = Column(Integer)
    street = Column(String)
    city = Column(String)
    postal_code = Column(String)

