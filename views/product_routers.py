from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db

from schemas.product import ProductCreate, ProductResponse, ProductUpdate
from controllers.product_controller import add_product, update_product, delete_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    return add_product(db, product_data)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_api(product_id: int, new_data: ProductUpdate, db: Session = Depends(get_db)):
    updated = update_product(db, product_id, new_data.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/{product_id}")
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    success = delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
