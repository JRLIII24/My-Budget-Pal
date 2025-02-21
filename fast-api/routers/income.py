from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import date

from schemas.income import IncomeCreate, IncomeUpdate, IncomeRead

router = APIRouter()

incomes_db = []

@router.post("/", response_model=IncomeRead)
async def create_income(income: IncomeCreate):
    # Example: Use income.id if provided, otherwise generate it
    existing_ids = [i.id for i in incomes_db if i.id is not None]
    new_id = (max(existing_ids) + 1) if existing_ids else 1
    new_income = IncomeRead(
        id=income.id if income.id else new_id,
        source=income.source,
        amount=income.amount,
        date=income.date
    )
    incomes_db.append(new_income)
    return new_income

@router.get("/", response_model=List[IncomeRead])
async def read_incomes(
    date_filter: Optional[date] = None,
    limit: int = 10,
    offset: int = 0
):
    filtered = incomes_db
    if date_filter is not None:
        filtered = [income for income in filtered if income.date == date_filter]
    return filtered[offset: offset + limit]

@router.get("/{income_id}", response_model=IncomeRead)
async def read_income(income_id: int):
    for income in incomes_db:
        if income.id == income_id:
            return income
    raise HTTPException(status_code=404, detail="Income not found")

@router.put("/{income_id}", response_model=IncomeRead)
async def update_income(income_id: int, updated_income: IncomeUpdate):
    for index, income in enumerate(incomes_db):
        if income.id == income_id:
            updated_income_data = income.copy(update=updated_income.dict(exclude_unset=True))
            incomes_db[index] = updated_income_data
            return updated_income_data
    raise HTTPException(status_code=404, detail="Income not found")

@router.delete("/{income_id}")
async def delete_income(income_id: int):
    for index, income in enumerate(incomes_db):
        if income.id == income_id:
            del incomes_db[index]
            return {"message": "Income deleted"}
    raise HTTPException(status_code=404, detail="Income not found")