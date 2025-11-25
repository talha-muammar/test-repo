from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.buyer import BuyerCreate, BuyerOut
from services.buyer_service import BuyerService
from repositories.buyer_repo import BuyerRepository

from db.database import get_db

router = APIRouter(prefix="/buyers", tags=["Buyers"])

@router.post("/register", response_model=BuyerOut)
def register_buyer(data: BuyerCreate, db: Session = Depends(get_db)):
    service = BuyerService(BuyerRepository(db))
    return service.register_buyer(data)
