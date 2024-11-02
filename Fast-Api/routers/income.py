from fastapi import APIRouter
from models import Income

router = APIRouter()

incomes = []
income_id_count = 1

@router.post("/incomes/", response_model=Income)
async def add_income(income: Income):
    global income_id_count
    income.id = income_id_count
    incomes.append(income)
    income_id_count += 1
    return income
