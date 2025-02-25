from pydantic import BaseModel, Field
from datetime import date as dt
from typing import Optional
class IncomeBase(BaseModel):
    source: str = Field(..., max_length=100)
    amount: float = Field(..., gt=0)
    date: dt

class IncomeCreate(IncomeBase):
    id: Optional[int] = None

class IncomeUpdate(IncomeBase):
    source: Optional[str] = Field(None, max_length=100)
    amount: Optional[float] = Field(None, gt=0)
    date: Optional[dt] = Field(None)

class IncomeRead(IncomeBase):
    id: int

    class Config:
        from_attributes = True
