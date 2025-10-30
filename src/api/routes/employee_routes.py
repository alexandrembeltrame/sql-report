from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.employee_schema import EmployeeCreate
from src.database.connection import get_db
from src.crud.employee_crud import (
    create_employee,
    get_employee,
    get_all_employees,
    delete_employee,
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=dict)
def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Cria um novo funcionário."""
    new_employee = create_employee(db, employee)
    return {
        "message": f"Funcionário '{new_employee.name}' criado com sucesso!",
        "id": new_employee.id,
    }


@router.get("/{employee_id}", response_model=dict)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    """Busca funcionário por ID."""
    employee = get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado.")
    return {
        "id": employee.id,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary,
        "performance": employee.performance,
    }


@router.get("/", response_model=list)
def list_employees(db: Session = Depends(get_db)):
    """Lista todos os funcionários."""
    employees = get_all_employees(db)
    return [
        {
            "id": e.id,
            "name": e.name,
            "department": e.department,
            "salary": e.salary,
            "performance": e.performance,
        }
        for e in employees
    ]


@router.delete("/{employee_id}", response_model=dict)
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    """Deleta funcionário por ID."""
    deleted = delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado.")
    return {"message": f"Funcionário ID {employee_id} removido com sucesso!"}
