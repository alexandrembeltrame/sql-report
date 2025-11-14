from pydantic import BaseModel
from datetime import date
from typing import Optional

class FinanceCreate(BaseModel):
  date: date
  description: str
  doc_number: str
  credit: Optional[float] = 0.0
  debit: Optional[float] = 0.0

  class FinanceBase(BaseModel):
    date: date
    description: str
    doc_number: str
    credit: Optional[float] = 0.0
    debit: Optional[float] = 0.0
  
  class FinanceCreate(FinanceBase):
    pass

  class FinanceUpdate(FinanceBase):
    date: date
    description: str
    doc_number: str
    credit: Optional[float] = 0.0
    debit: Optional[float] = 0.0

  class FinanceResponse(FinanceBase):
    id: int

    class Config:
      from_attributes = True