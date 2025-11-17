from pydantic import BaseModel, ConfigDict

class EmployeeBase(BaseModel):
  name: str
  department: str
  salary: float
  performance: int

class EmployeeCreate(EmployeeBase):
  pass

class EmployeeOut(EmployeeBase):
  id: int

  model_config = ConfigDict(from_attributes=True)
  