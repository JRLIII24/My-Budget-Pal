from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Income as IncomeDB
from pydantic_models import Income
from typing import List

router = APIRouter()

@router.post("/incomes/", response_model=Income)
async def add_income(income: Income, db: Session = Depends(get_db)):
    new_income = IncomeDB(
        source=income.source,
        amount=income.amount,
        date=income.date,
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income

@router.get("/incomes/", response_model=List[Income])
async def get_incomes(db: Session = Depends(get_db)):
    return db.query(IncomeDB).all()

@router.get("/incomes/{income_id}", response_model=Income)
async def get_income_by_id(income_id: int, db: Session = Depends(get_db)):
    income = db.query(IncomeDB).filter(IncomeDB.id == income_id).first()
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.put("/incomes/{income_id}", response_model=Income)
async def update_income(income_id: int, income: Income, db: Session = Depends(get_db)):
    existing_income = db.query(IncomeDB).filter(IncomeDB.id == income_id).first()
    if not existing_income:
        raise HTTPException(status_code=404, detail="Income not found")

    existing_income.source = income.source
    existing_income.amount = income.amount
    existing_income.date = income.date
    db.commit()
    db.refresh(existing_income)
    return existing_income

@router.delete("/incomes/{income_id}")
async def delete_income(income_id: int, db: Session = Depends(get_db)):
    income = db.query(IncomeDB).filter(IncomeDB.id == income_id).first()
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    db.delete(income)
    db.commit()
    return {"message": "Income successfully deleted"}