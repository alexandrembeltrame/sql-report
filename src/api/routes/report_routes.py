from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.database.models.models import Employee, Finance  # <-- aqui trocamos o modelo
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter(prefix="/reports", tags=["Reports"])

# Adicione o middleware CORS
def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Permitir o frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@router.get("/employees")
def get_employees_report(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return {"results": employees}

@router.get("/finances")
def get_finances_report(db: Session = Depends(get_db)):
    finances = db.query(Finance).all()
    return {"results": finances}