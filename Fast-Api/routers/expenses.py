from fastapi import APIRouter
from models import Expense

router = APIRouter()

expenses = []
expense_id_count = 1

@router.post("/expenses/", response_model=Expense)
async def create_expense(expense: Expense):
    global expense_id_count
    expense.id = expense_id_count
    expenses.append(expense)
    expense_id_count += 1
    return expense