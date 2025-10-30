#src/api/routes/report_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.reports.report_queries import get_employee_report

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/employees")
def employee_report(db: Session = Depends(get_db)):
  """
  Retorna um relatório simples de funcionários (exemplo base)
  """
  data = get_employee_report(db)
  return {"count": len(data), "results": data}