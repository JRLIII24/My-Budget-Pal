from pydantic import BaseModel
from datetime import date
from typing import Optional

class Income(BaseModel):
    id: int
    source: str
    amount: float
    date: date
