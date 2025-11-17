from typing import Annotated
from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    department: Annotated[str, Field(min_length=2)]
    salary: Annotated[float, Field(ge=0)]
    performance: Annotated[float, Field(ge=0, le=10)]

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Annotated[str, Field(min_length=1)] | None = None
    department: Annotated[str, Field(min_length=2)] | None = None
    salary: Annotated[float, Field(ge=0)] | None = None
    performance: Annotated[float, Field(ge=0, le=10)] | None = None