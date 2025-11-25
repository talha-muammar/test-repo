from repositories.buyer_repo import BuyerRepository
from core.security import hash_password

class BuyerService:
    def __init__(self, repo: BuyerRepository):
        self.repo = repo

    def register_buyer(self, buyer_data):
        #buyer_data.password = hash_password(buyer_data.password)
        return self.repo.create_buyer(buyer_data)

    def get_buyer_by_email(self, email):
        return self.repo.get_by_email(email)
