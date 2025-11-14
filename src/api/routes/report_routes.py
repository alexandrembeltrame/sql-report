from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.models.models import Employee, Finance  # <-- aqui trocamos o modelo


router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/employees")
def get_employees_report(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return {"results": employees}

@router.get("/finances")
def get_finances_report(db: Session = Depends(get_db)):
    finances = db.query(Finance).all()
    return {"results": finances}