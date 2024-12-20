from pydantic import BaseModel
from typing import Optional
from datetime import date

class Expense(BaseModel):
    id: Optional[int] = None
    name: str
    category: str
    amount: float
    date: date

    class Config:
        orm_mode = True


class Income(BaseModel):
    id: Optional[int] = None
    source: str
    amount: float
    date: date

    class Config:
        orm_mode = True


class Bill(BaseModel):
    id: Optional[int] = None
    name: str
    amount: float
    due_date: date

    class Config:
        orm_mode = True