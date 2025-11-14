from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.models.models import Finance
from src.schemas.finance_schema import FinanceCreate

router = APIRouter(prefix="/finances", tags=["Finances"])

@router.get("/")
def get_finances(db: Session = Depends(get_db)):
  return db.query(Finance).all()

@router.post("/")
def create_finance(finance: FinanceCreate, db: Session = Depends(get_db)):
  new_finance = Finance(
    date=finance.date,
    description=finance.description,
    doc_number=finance.doc_number,
    credit=finance.credit,
    debit=finance.debit
  )
  db.add(new_finance)
  db.commit()
  db.refresh(new_finance)
  return new_finance

