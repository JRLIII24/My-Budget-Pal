from fastapi import APIRouter, HTTPException
from models import Bill
from typing import List

router = APIRouter()

bills = []
bills_id_count = 1

@router.post("/bills/", response_model=Bill)
async def create_bill(bill: Bill):
    global bills_id_count
    bill.id = bills_id_count
    bills.append(bill)
    bills_id_count += 1
    return bill

@router.put("/bills/{bills_id}", response_model=Bill)
async def update_bill(bills_id: int, bill: Bill):
    for existing_bill in bills:
        if existing_bill.id == bills_id:
            existing_bill.name = bill.name
            existing_bill.amount = bill.amount
            existing_bill.due_date = bill.due_date
            return existing_bill

    raise HTTPException(status_code=404, detail="Bill not found")

@router.get("/bills/", response_model=List[Bill])
async def get_bills():
    return bills

@router.get("/bills/{bills_id}", response_model=Bill)
async def get_bill_id(bills_id: int):
    for bill in bills:
        if bill.id == bills_id:
            return bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.delete("/bills/{bills_id}")
async def delete_bill(bills_id: int):
    for bill in bills:
        if bill.id == bills_id:
            bills.remove(bill)
            return {"message": "Bill successfully deleted"}
    raise HTTPException(status_code=404, detail="Bill not found")