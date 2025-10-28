from sqlalchemy.orm import Session
from src.models.employee_model import Employee
from src.schemas.employee_schema import EmployeeCreate, EmployeeUpdate

class EmployeeRepository:
    @staticmethod
    def get_all(db: Session):
        """Retorna todos os funcionários"""
        return db.query(Employee).all()

    @staticmethod
    def get_by_id(db: Session, employee_id: int):
        """Busca funcionário por ID"""
        return db.query(Employee).filter(Employee.id == employee_id).first()

    @staticmethod
    def create(db: Session, employee_data: EmployeeCreate):
        """Cria um novo funcionário"""
        new_employee = Employee(**employee_data.model_dump())
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    @staticmethod
    def update(db: Session, employee_id: int, employee_data: EmployeeUpdate):
        """Atualiza um funcionário existente"""
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee is None:
            return None
        
        for key, value in employee_data.model_dump().items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)
        return employee

    @staticmethod
    def delete(db: Session, employee_id: int):
        """Deleta um funcionário"""
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee is None:
            return None

        db.delete(employee)
        db.commit()
        return employee
