from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import date
from schemas.savings import SavingsCreate, SavingsUpdate, SavingsRead

router = APIRouter()

savings_db = []

@router.post("/", response_model=SavingsRead)
async def create_savings(savings: SavingsCreate):
    existing_ids = [s.id for s in savings_db if s.id is not None]
    new_id = (max(existing_ids) + 1) if existing_ids else 1
    new_savings = SavingsRead(
        id=savings.id if savings.id else new_id,
        description=savings.description,
        amount=savings.amount,
        date=savings.date
    )
    savings_db.append(new_savings)
    return new_savings

@router.get("/", response_model=List[SavingsRead])
async def read_savings(
    date_filter: Optional[date] = None,
    limit: int = 10,
    offset: int = 0
):
    filtered = savings_db
    if date_filter is not None:
        filtered = [saving for saving in filtered if saving.date == date_filter]
    return filtered[offset: offset + limit]

@router.get("/{savings_id}", response_model=SavingsRead)
async def read_savings_item(savings_id: int):
    for saving in savings_db:
        if saving.id == savings_id:
            return saving
    raise HTTPException(status_code=404, detail="Savings not found")

@router.put("/{savings_id}", response_model=SavingsRead)
async def update_savings(savings_id: int, updated_savings: SavingsUpdate):
    for index, saving in enumerate(savings_db):
        if saving.id == savings_id:
            updated_savings_data = saving.copy(update=updated_savings.dict(exclude_unset=True))
            savings_db[index] = updated_savings_data
            return updated_savings_data
    raise HTTPException(status_code=404, detail="Savings not found")

@router.delete("/{savings_id}")
async def delete_savings(savings_id: int):
    for index, saving in enumerate(savings_db):
        if saving.id == savings_id:
            del savings_db[index]
            return {"message": "Savings deleted"}
    raise HTTPException(status_code=404, detail="Savings not found")