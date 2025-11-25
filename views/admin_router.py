from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.admin import AdminLogin, AdminOut
from services.admin_service import AdminService
from repositories.admin_repo import AdminRepository
from db.database import get_db

router = APIRouter(prefix="/admin", tags=["Admins"])

@router.post("/login", response_model=AdminOut)
def admin_login(data: AdminLogin, db: Session = Depends(get_db)):
    service = AdminService(AdminRepository(db))
    admin_data = service.login_admin(data.email, data.password)
    if not admin_data:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return admin_data
