from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date

from schemas.bill import Bill

router = APIRouter()

bills_db = []


@router.post("/", response_model=Bill)
def create_bill(bill: Bill):
    for item in bills_db:
        if item.id == bill.id:
            raise HTTPException(status_code=400, detail="Bill with this ID already exists")
    bills_db.append(bill)
    return bill

@router.get("/", response_model=List[Bill])
def read_bills():
    return bills_db

@router.get("/{bill_id}", response_model=Bill)
def read_bill(bill_id: int):
    for bill in bills_db:
        if bill.id == bill_id:
            return bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.put("/{bill_id}", response_model=Bill)
def update_bill(bill_id: int, updated_bill: Bill):
    for index, bill in enumerate(bills_db):
        if bill.id == bill_id:
            bills_db[index] = updated_bill
            return updated_bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.delete("/{bill_id}")
def delete_bill(bill_id: int):
    for index, bill in enumerate(bills_db):
        if bill.id == bill_id:
            del bills_db[index]
            return {"message": "Bill deleted"}
    raise HTTPException(status_code=404, detail="Bill not found")