from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date
from schemas.savings import Savings

router = APIRouter()

savings_db = []

@router.post("/savings/", response_model=Savings)
def create_savings(savings: Savings):
    for item in savings_db:
        if item.id == savings.id:
            raise HTTPException(status_code=400, detail="Savings with this ID already exists")
    savings_db.append(savings)
    return savings

@router.get("/savings/", response_model=List[Savings])
def read_savings():
    return savings_db

@router.get("/savings/{savings_id}", response_model=Savings)
def read_savings_item(savings_id: int):
    for saving in savings_db:
        if saving.id == savings_id:
            return saving
    raise HTTPException(status_code=404, detail="Savings not found")

@router.put("/savings/{savings_id}", response_model=Savings)
def update_savings(savings_id: int, updated_savings: Savings):
    for index, saving in enumerate(savings_db):
        if saving.id == savings_id:
            savings_db[index] = updated_savings
            return updated_savings
    raise HTTPException(status_code=404, detail="Savings not found")

@router.delete("/savings/{savings_id}")
def delete_savings(savings_id: int):
    for index, saving in enumerate(savings_db):
        if saving.id == savings_id:
            del savings_db[index]
            return {"message": "Savings deleted"}
    raise HTTPException(status_code=404, detail="Savings not found")