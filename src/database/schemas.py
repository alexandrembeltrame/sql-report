from pydantic import BaseModel

class EmployeeBase(BaseModel):
  name: str
  department: str
  salary: float
  performance: int

  class EmployeeCreate(EmployeeBase):
    pass

  class EmployeeOut(EmployeeBase):
    id: int

    class Config:
      orm_mode = True
  