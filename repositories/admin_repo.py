from sqlalchemy.orm import Session
from models.admin import Admin

class AdminRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(Admin).filter(Admin.email == email).first()
