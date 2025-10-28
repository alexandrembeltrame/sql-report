from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.employee_schema import EmployeeCreate
from src.models.employee import Employee
from src.crud.employee_crud import create_employee, get_all_employees
from src.core.database import get_db

router = APIRouter(prefix="/employees", tags=["employees"])

# Criar novo funcionário
@router.post("/", response_model=dict)
def create_employee_route(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        employee_db = create_employee(db, employee)
        return {"message": "Funcionário criado com sucesso!", "employee_id": employee_db.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Listar todos os funcionários
@router.get("/", response_model=list[dict])
def list_employees_route(db: Session = Depends(get_db)):
    employees = get_all_employees(db)
    return [{"id": emp.id, "name": emp.name, "department": emp.department, "salary": emp.salary, "performance": emp.performance} for emp in employees]
