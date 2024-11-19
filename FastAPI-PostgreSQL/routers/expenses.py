from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Expense as ExpenseDB
from pydantic_models import Expense
from typing import List

router = APIRouter()

@router.post("/expenses/", response_model=Expense)
async def create_expense(expense: Expense, db: Session = Depends(get_db)):
    new_expense = ExpenseDB(
        name=expense.name,
        category=expense.category,
        amount=expense.amount,
        date=expense.date,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/expenses/", response_model=List[Expense])
async def get_expenses(db: Session = Depends(get_db)):
    return db.query(ExpenseDB).all()

@router.get("/expenses/{expense_id}", response_model=Expense)
async def get_expense_id(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/expenses/{expense_id}", response_model=Expense)
async def update_expense(expense_id: int, expense: Expense, db: Session = Depends(get_db)):
    existing_expense = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not existing_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    existing_expense.name = expense.name
    existing_expense.category = expense.category
    existing_expense.amount = expense.amount
    existing_expense.date = expense.date
    db.commit()
    db.refresh(existing_expense)
    return existing_expense

@router.delete("/expenses/{expense_id}")
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense successfully deleted"}