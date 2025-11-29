from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    image_url = Column(String)
    date_added = Column(DateTime, default=datetime.utcnow)
    is_available = Column(Boolean, default=True)

    # Category relationship
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    category = relationship("Category", back_populates="products")

    # Inventory relationship
    inventory_id = Column(Integer, ForeignKey("inventories.inventory_id"), nullable=True)
    inventory = relationship("Inventory", back_populates="products")
