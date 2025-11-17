# src/api/routes/health_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db

router = APIRouter()

@router.get("/health/db")
def check_db(db: Session = Depends(get_db)):
    try:
        # SELECT 1 é o teste mais simples de vida do banco
        db.execute("SELECT 1")
        return {"status": "up"}
    except Exception:
        return {"status": "down"}
