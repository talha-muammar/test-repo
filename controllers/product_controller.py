from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate


def add_product(db: Session, product_data: ProductCreate) -> Product:
    """Create and save a new product."""
    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock=product_data.stock,
        image_url=product_data.image_url,
        category_id=product_data.category_id,
        inventory_id=product_data.inventory_id,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def update_product(db: Session, product_id: int, fields: dict) -> Product | None:
    """Update a product partially by receiving a dict of fields."""
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        return None

    # Update only provided fields
    for key, value in fields.items():
        if hasattr(product, key):
            setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> bool:
    """Soft delete or hard delete a product."""
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        return False

    db.delete(product)
    db.commit()
    return True
