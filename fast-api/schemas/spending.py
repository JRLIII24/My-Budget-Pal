from pydantic import BaseModel
from datetime import date
from typing import Optional

class Spending(BaseModel):
    id: int
    category: str
    amount: float
    date: date