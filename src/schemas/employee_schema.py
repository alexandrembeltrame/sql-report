from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
  name: str = Field(..., min_length=2, max_length=100)
  department: str = Field(..., min_length=2, max_length=50)
  salary: float = Field(..., gt=0)
  performance: int = Field(..., ge=0, le=10)

class EmployeeCreate(EmployeeBase):
  """Schema usado ao criar um novo funcionário"""
  pass

class EmployeeUpdate(EmployeeBase):
  """Schema usado ao atualizar um funcionário existente"""
  pass

class EmployeeOut(EmployeeBase):
  """Schema de saída (resposta da API)"""
  id: int

  class config:
    orm_mode = True