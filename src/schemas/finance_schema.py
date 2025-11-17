from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class FinanceBase(BaseModel):
    date: date
    description: str
    doc_number: str
    credit: Optional[float] = 0.0
    debit: Optional[float] = 0.0

class FinanceCreate(FinanceBase):
    pass

class FinanceUpdate(FinanceBase):
    pass

class FinanceResponse(FinanceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)