from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db.database import Base


class Inventory(Base):
    __tablename__ = "inventories"

    inventory_id = Column(Integer, primary_key=True, index=True)
    low_stock_threshold = Column(Integer, default=5)

    # Relationship → products in this inventory
    products = relationship("Product", back_populates="inventory")
