from pydantic import BaseModel, Field
from datetime import date as dt
from typing import Optional

class SavingsBase(BaseModel):
    description: str = Field(..., max_length=200)
    amount: float = Field(..., gt=0)
    date: dt

class SavingsCreate(SavingsBase):
    id: Optional[int] = None

class SavingsUpdate(SavingsBase):
    description: Optional[str] = Field(None, max_length=200)
    amount: Optional[float] = Field(None, gt=0)
    date: Optional[dt] = None

class SavingsRead(SavingsBase):
    id: int

    class Config:
        from_attributes = True