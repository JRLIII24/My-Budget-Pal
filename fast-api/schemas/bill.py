from pydantic import BaseModel
from datetime import date
from typing import Optional

class Bill(BaseModel):
    id: int
    name: str
    due_date: date
    amount: float
    paid: bool = False
