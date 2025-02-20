from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date

from schemas.income import Income

router = APIRouter()


incomes_db = []



@router.post("/", response_model=Income)
def create_income(income: Income):
    for item in incomes_db:
        if item.id == income.id:
            raise HTTPException(status_code=400, detail="Income with this ID already exists")
    incomes_db.append(income)
    return income

@router.get("/", response_model=List[Income])
def read_incomes():
    return incomes_db

@router.get("/{income_id}", response_model=Income)
def read_income(income_id: int):
    for income in incomes_db:
        if income.id == income_id:
            return income
    raise HTTPException(status_code=404, detail="Income not found")

@router.put("/{income_id}", response_model=Income)
def update_income(income_id: int, updated_income: Income):
    for index, income in enumerate(incomes_db):
        if income.id == income_id:
            incomes_db[index] = updated_income
            return updated_income
    raise HTTPException(status_code=404, detail="Income not found")

@router.delete("/{income_id}")
def delete_income(income_id: int):
    for index, income in enumerate(incomes_db):
        if income.id == income_id:
            del incomes_db[index]
            return {"message": "Income deleted"}
    raise HTTPException(status_code=404, detail="Income not found")