from pydantic import BaseModel
from datetime import date
from typing import Optional

class Savings(BaseModel):
    id: int
    description: str
    amount: float
    date: date