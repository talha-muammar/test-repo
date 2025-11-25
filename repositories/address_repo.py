from sqlalchemy.orm import Session
from models.address import Address

class AddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_address(self, address_data):
        address = Address(
            house_no=address_data.house_no,
            street=address_data.street,
            city=address_data.city,
            postal_code=address_data.postal_code
        )
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address
