from pydantic import BaseModel, Field
from datetime import date as dt
from typing import Optional

class SpendingBase(BaseModel):
    category: str = Field(..., max_length=50)
    amount: float = Field(..., gt=0)
    date: dt

class SpendingCreate(SpendingBase):
    id: Optional[int] = None

class SpendingUpdate(SpendingBase):
    category: Optional[str] = Field(None, max_length=50)
    amount: Optional[float] = Field(None, gt=0)
    date: Optional[dt] = None

class SpendingRead(SpendingBase):
    id: int

    class Config:
        orm_mode = True