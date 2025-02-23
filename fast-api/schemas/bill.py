from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BillBase(BaseModel):
    name: str = Field(..., max_length=100)
    due_date: date
    amount: float = Field(..., gt=0)
    paid: bool = False

class BillCreate(BillBase):
    # ID is optional since it's typically generated by the database
    id: Optional[int] = None

class BillUpdate(BillBase):
    # Optional fields for partial updates
    name: Optional[str] = Field(None, max_length=100)
    due_date: Optional[date] = None
    amount: Optional[float] = Field(None, gt=0)
    paid: Optional[bool] = None

class BillRead(BillBase):
    id: int

    class Config:
        orm_mode = True
