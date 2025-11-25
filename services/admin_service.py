from repositories.admin_repo import AdminRepository
from core.security import verify_password

class AdminService:
    def __init__(self, repo: AdminRepository):
        self.repo = repo

    def login_admin(self, email, password):
        admin = self.repo.get_by_email(email)
        if not admin:
            return None
        #if not verify_password(password, admin.password):
            return None
        # Example token payload
        return {"id": admin.id, "name": admin.name, "role": admin.role}
