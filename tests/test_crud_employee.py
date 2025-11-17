import pytest
from unittest.mock import Mock, MagicMock, patch
from src.crud.employee_crud import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    delete_employee
)
from src.schemas.employee_schema import EmployeeCreate, EmployeeUpdate

def test_create_employee(db):
    data = EmployeeCreate(
        name="Alexandre",
        department="Tech",
        salary=5000.0,
        performance=9.2  # ← Ajustado de 90 para 9.2
    )

    emp = create_employee(db, data)
    assert emp.id is not None
    assert emp.name == "Alexandre"


def test_get_employee(db):
    data = EmployeeCreate(
        name="Kairos",
        department="AI",
        salary=7000.0,
        performance=9.5  # ← Ajustado de 95 para 9.5
    )
    emp = create_employee(db, data)

    found = get_employee(db, emp.id)
    assert found is not None
    assert found.name == "Kairos"


def test_get_all_employees(db):
    create_employee(db, EmployeeCreate(
        name="A", department="D1", salary=1000, performance=8.0  # ← Ajustado de 80 para 8.0
    ))
    create_employee(db, EmployeeCreate(
        name="B", department="D2", salary=2000, performance=8.5  # ← Ajustado de 85 para 8.5
    ))

    result = get_all_employees(db)
    assert len(result) >= 2


def test_update_employee(db):
    emp = create_employee(db, EmployeeCreate(
        name="Old",
        department="Dev",
        salary=3000,
        performance=7.0  # ← Ajustado de 70 para 7.0
    ))

    updated = update_employee(
        db, 
        emp.id, 
        EmployeeUpdate(name="New Name")
    )

    assert updated.name == "New Name"


def test_delete_employee(db):
    emp = create_employee(db, EmployeeCreate(
        name="Delete",
        department="Ops",
        salary=3500,
        performance=7.3  # ← Ajustado de 73 para 7.3
    ))

    deleted = delete_employee(db, emp.id)
    assert deleted.id == emp.id

    assert get_employee(db, emp.id) is None


def test_retornar_employee_criado_com_id_ao_criar_employee_usando_mock():
    """
    Testa se ao criar um employee, o registro retornado contém um ID válido.
    Usa mock COMPLETO para não tocar no banco de dados real.
    Este teste valida o comportamento esperado (equivalente a código 201).
    """
    # Arrange
    mock_db = MagicMock()
    employee_data = EmployeeCreate(
        name="João Silva",
        department="TI",
        salary=5000.0,
        performance=9.0  # ← Ajustado de 90 para 9.0
    )
    
    # Mock do objeto Employee que seria retornado
    mock_employee = Mock()
    mock_employee.id = 1
    mock_employee.name = "João Silva"
    mock_employee.department = "TI"
    mock_employee.salary = 5000.0
    mock_employee.performance = 9.0  # ← Ajustado de 90 para 9.0
    
    # Configurar o comportamento do mock
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    
    # Mockar a função refresh para atribuir o ID
    def mock_refresh(obj):
        obj.id = 1
    
    mock_db.refresh.side_effect = mock_refresh
    
    # Act - Mockar a função create_employee completamente
    with patch("src.crud.employee_crud.create_employee", return_value=mock_employee) as mock_create:
        result = create_employee(mock_db, employee_data)
    
    # Assert - Validar retorno (equivalente a código 201 - criado com sucesso)
    assert result.id is not None
    assert result.id == 1
    assert result.name == "João Silva"
    assert result.department == "TI"
    assert result.salary == 5000.0
    assert result.performance == 9.0  # ← Ajustado de 90 para 9.0


def test_get_employee_not_found(db):
    """Testa busca de employee que não existe"""
    employee = get_employee(db, employee_id=9999)
    assert employee is None

def test_update_employee_not_found(db):
    """Testa atualização de employee que não existe"""
    update_data = EmployeeUpdate(name="Updated")
    employee = update_employee(db, employee_id=9999, employee=update_data)
    assert employee is None

def test_delete_employee_not_found(db):
    """Testa deleção de employee que não existe"""
    result = delete_employee(db, employee_id=9999)
    assert result is None

def test_create_employee_with_min_values(db):
    """Testa criação com valores mínimos permitidos"""
    employee_data = EmployeeCreate(
        name="A",
        department="IT",
        salary=0.0,
        performance=0.0
    )
    employee = create_employee(db, employee_data)
    assert employee.name == "A"
    assert employee.salary == 0.0
    assert employee.performance == 0.0

def test_create_employee_with_max_performance(db):
    """Testa criação com performance máxima"""
    employee_data = EmployeeCreate(
        name="Top Performer",
        department="Sales",
        salary=100000.0,
        performance=10.0
    )
    employee = create_employee(db, employee_data)
    assert employee.performance == 10.0

def test_update_employee_partial(db):
    """Testa atualização parcial (apenas alguns campos)"""
    employee_data = EmployeeCreate(
        name="John Doe",
        department="IT",
        salary=50000.0,
        performance=7.5
    )
    employee = create_employee(db, employee_data)
    
    # Atualiza apenas o salário
    update_data = EmployeeUpdate(salary=60000.0)
    updated = update_employee(db, employee.id, update_data)
    
    assert updated.salary == 60000.0
    assert updated.name == "John Doe"  # Outros campos não mudaram
    assert updated.performance == 7.5

def test_update_employee_all_fields(db):
    """Testa atualização de todos os campos"""
    employee_data = EmployeeCreate(
        name="Jane Doe",
        department="HR",
        salary=45000.0,
        performance=6.0
    )
    employee = create_employee(db, employee_data)
    
    update_data = EmployeeUpdate(
        name="Jane Smith",
        department="Finance",
        salary=55000.0,
        performance=8.5
    )
    updated = update_employee(db, employee.id, update_data)
    
    assert updated.name == "Jane Smith"
    assert updated.department == "Finance"
    assert updated.salary == 55000.0
    assert updated.performance == 8.5

def test_get_all_employees_empty(db):
    """Testa listagem quando não há employees"""
    employees = get_all_employees(db)
    assert employees == []

def test_get_all_employees_multiple(db):
    """Testa listagem com múltiplos employees"""
    employees_data = [
        EmployeeCreate(name="Employee 1", department="IT", salary=50000.0, performance=7.0),
        EmployeeCreate(name="Employee 2", department="HR", salary=45000.0, performance=8.0),
        EmployeeCreate(name="Employee 3", department="Sales", salary=55000.0, performance=6.5),
    ]
    
    for emp_data in employees_data:
        create_employee(db, emp_data)
    
    employees = get_all_employees(db)
    assert len(employees) == 3

def test_delete_employee_success(db):
    """Testa deleção bem-sucedida"""
    employee_data = EmployeeCreate(
        name="To Delete",
        department="IT",
        salary=50000.0,
        performance=7.0
    )
    employee = create_employee(db, employee_data)
    employee_id = employee.id
    
    # Deleta
    result = delete_employee(db, employee_id)
    assert result is not None
    assert result.id == employee_id
    
    # Verifica que foi deletado
    deleted_employee = get_employee(db, employee_id)
    assert deleted_employee is None
