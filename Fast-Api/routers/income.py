from fastapi import APIRouter, HTTPException
from models import Income
from typing import List, Optional
from datetime import date

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

@router.put("/incomes/{income_id}", response_model=Income)
async def update_income(income_id: int, income: Income):
    for existing_income in incomes:
        if existing_income.id == income_id:
            existing_income.source = income.source
            existing_income.amount = income.amount
            existing_income.date = income.date
            return existing_income
    raise HTTPException(status_code=404, detail="Income not found")

@router.get("/incomes/", response_model=List[Income])
async def get_incomes():
    return incomes

@router.get("/incomes/{income_id}", response_model=Income)
async def get_income_by_id(income_id: int):
    for income in incomes:
        if income.id == income_id:
            return income
    raise HTTPException(status_code=404, detail="Income not found")

@router.delete("/incomes/{income_id}")
async def delete_income(income_id: int):
    for income in incomes:
        if income.id == income_id:
            incomes.remove(income)
            return {"message": "Income successfully deleted"}
    raise HTTPException(status_code=404, detail="Income not found")