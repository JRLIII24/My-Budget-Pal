from pydantic import BaseModel
from datetime import date
from typing import Optional

# Income Schemas
class IncomeBase(BaseModel):
    source: str
    amount: float
    date: date

class IncomeCreate(IncomeBase):
    pass

class IncomeResponse(IncomeBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True

# Savings Schemas
class SavingsBase(BaseModel):
    description: str
    amount: float
    date: date

class SavingsCreate(SavingsBase):
    pass

class SavingsResponse(SavingsBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True

# Spending Schemas
class SpendingBase(BaseModel):
    category: str
    amount: float
    date: date

class SpendingCreate(SpendingBase):
    pass

class SpendingResponse(SpendingBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True

# Bill Schemas
class BillBase(BaseModel):
    name: str
    due_date: date
    amount: float
    paid: Optional[int] = 0

class BillCreate(BillBase):
    pass

class BillResponse(BillBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True