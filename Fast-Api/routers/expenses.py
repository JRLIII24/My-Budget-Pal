from fastapi import APIRouter, HTTPException
from models import Expense
from typing import List

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

@router.put("/expenses/{expenses_id}", response_model=Expense)
async def update_expense(expense_id: int, expense: Expense):
    for existing_expense in expenses:
        if existing_expense.id == expense_id:
            existing_expense.name = expense.name
            existing_expense.category =expense.category
            existing_expense.amount = expense.amount
            existing_expense.date = expense.date
            return existing_expense

    raise HTTPException(status_code=404, detail="Expense not found")

@router.get("/expenses/", response_model=List[Expense])
async def get_expenses():
    return expenses

@router.get("/expenses/{expenses_id}", response_model=Expense)
async def get_expense_id(expenses_id: int):
    for e in expenses:
        if e.id == expenses_id:
            return e
    raise HTTPException(status_code=404, detail="Expense not found")

@router.delete("/expenses/{expense_id}")
async def delete_expense(expenses_id: int):
    # Find the expense by ID
    for expense in expenses:
        if expense.id == expenses_id:
            expenses.remove(expense)
            return {"message": "Expense successfully deleted"}
    # If expense not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Expense not found")