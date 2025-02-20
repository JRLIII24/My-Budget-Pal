from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date

from schemas.spending import Spending

router = APIRouter()


spendings_db = []



@router.post("/", response_model=Spending)
def create_spending(spending: Spending):
    for item in spendings_db:
        if item.id == spending.id:
            raise HTTPException(status_code=400, detail="Spending with this ID already exists")
    spendings_db.append(spending)
    return spending

@router.get("/", response_model=List[Spending])
def read_spendings():
    return spendings_db

@router.get("/{spending_id}", response_model=Spending)
def read_spending(spending_id: int):
    for spending in spendings_db:
        if spending.id == spending_id:
            return spending
    raise HTTPException(status_code=404, detail="Spending not found")

@router.put("/{spending_id}", response_model=Spending)
def update_spending(spending_id: int, updated_spending: Spending):
    for index, spending in enumerate(spendings_db):
        if spending.id == spending_id:
            spendings_db[index] = updated_spending
            return updated_spending
    raise HTTPException(status_code=404, detail="Spending not found")

@router.delete("/{spending_id}")
def delete_spending(spending_id: int):
    for index, spending in enumerate(spendings_db):
        if spending.id == spending_id:
            del spendings_db[index]
            return {"message": "Spending deleted"}
    raise HTTPException(status_code=404, detail="Spending not found")