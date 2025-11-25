from sqlalchemy.orm import Session
from models.buyer import Buyer
from repositories.address_repo import AddressRepository

class BuyerRepository:
    def __init__(self, db: Session):
        self.db = db
        self.address_repo = AddressRepository(db)

    def create_buyer(self, buyer_data):
        # Create Address first
        address = self.address_repo.create_address(buyer_data.address)

        buyer = Buyer(
            name=buyer_data.name,
            email=buyer_data.email,
            phone=buyer_data.phone,
            password=buyer_data.password,
            address_id=address.id
        )
        self.db.add(buyer)
        self.db.commit()
        self.db.refresh(buyer)
        return buyer

    def get_by_email(self, email: str):
        return self.db.query(Buyer).filter(Buyer.email == email).first()
