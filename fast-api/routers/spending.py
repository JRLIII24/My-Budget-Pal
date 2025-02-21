from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import date
from schemas.spending import SpendingCreate, SpendingUpdate, SpendingRead

router = APIRouter()

spendings_db = []

@router.post("/", response_model=SpendingRead)
async def create_spending(spending: SpendingCreate):
    existing_ids = [s.id for s in spendings_db if s.id is not None]
    new_id = (max(existing_ids) + 1) if existing_ids else 1
    new_spending = SpendingRead(
        id=spending.id if spending.id else new_id,
        category=spending.category,
        amount=spending.amount,
        date=spending.date
    )
    spendings_db.append(new_spending)
    return new_spending

@router.get("/", response_model=List[SpendingRead])
async def read_spendings(
    date_filter: Optional[date] = None,
    amount_filter: Optional[float] = None,
    limit: int = 10,
    offset: int = 0
):
    filtered = spendings_db
    if date_filter is not None:
        filtered = [spending for spending in filtered if spending.date == date_filter]
    if amount_filter is not None:
        filtered = [spending for spending in filtered if spending.amount == amount_filter]
    return filtered[offset: offset + limit]

@router.get("/{spending_id}", response_model=SpendingRead)
async def read_spending(spending_id: int):
    for spending in spendings_db:
        if spending.id == spending_id:
            return spending
    raise HTTPException(status_code=404, detail="Spending not found")

@router.put("/{spending_id}", response_model=SpendingRead)
async def update_spending(spending_id: int, updated_spending: SpendingUpdate):
    for index, spending in enumerate(spendings_db):
        if spending.id == spending_id:
            updated_spending_data = spending.copy(update=updated_spending.dict(exclude_unset=True))
            spendings_db[index] = updated_spending_data
            return updated_spending_data
    raise HTTPException(status_code=404, detail="Spending not found")

@router.delete("/{spending_id}")
async def delete_spending(spending_id: int):
    for index, spending in enumerate(spendings_db):
        if spending.id == spending_id:
            del spendings_db[index]
            return {"message": "Spending deleted"}
    raise HTTPException(status_code=404, detail="Spending not found")