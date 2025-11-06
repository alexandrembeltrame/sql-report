from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.models.models import Employee  # <-- aqui trocamos o modelo

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/employees")
def get_employees_report(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return {"results": employees}
