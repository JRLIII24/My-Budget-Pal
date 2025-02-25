from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BillBase(BaseModel):
    name: str = Field(..., max_length=100)
    due_date: date
    amount: float = Field(..., gt=0)
    paid: bool = False
    account_id: Optional[int] = None

class BillCreate(BillBase):
    # account_id is optional when creating an entry (set internally)
    pass

class BillUpdate(BillBase):
    # Optional fields for partial updates, account_id can be optionally updated as well
    name: Optional[str] = Field(None, max_length=100)
    due_date: Optional[date] = None
    amount: Optional[float] = Field(None, gt=0)
    paid: Optional[bool] = None
    account_id: Optional[int] = None

class BillRead(BillBase):
    id: int
    account_id: int  # Now required as part of the read model

    class Config:
        from_attributes = True
