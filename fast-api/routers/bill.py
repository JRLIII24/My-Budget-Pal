from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import date

from schemas.bill import BillCreate, BillUpdate, BillRead

router = APIRouter()
bills_db = []

@router.post("/", response_model=BillRead)
async def create_bill(bill: BillCreate):
    # Example: Use bill.id if provided, otherwise generate it
    existing_ids = [b.id for b in bills_db if b.id is not None]
    new_id = (max(existing_ids) + 1) if existing_ids else 1
    new_bill = BillRead(
        id=bill.id if bill.id else new_id,
        name=bill.name,
        due_date=bill.due_date,
        amount=bill.amount,
        paid=bill.paid
    )
    bills_db.append(new_bill)
    return new_bill

@router.get("/", response_model=List[BillRead])
async def read_bills(
    date_filter: Optional[date] = None,
    amount_filter: Optional[float] = None,
    limit: int = 10,
    offset: int = 0
):
    filtered = bills_db
    if date_filter is not None:
        filtered = [b for b in filtered if b.due_date == date_filter]
    if amount_filter is not None:
        filtered = [b for b in filtered if b.amount == amount_filter]
    return filtered[offset: offset + limit]

@router.get("/{bill_id}", response_model=BillRead)
async def read_bill(bill_id: int):
    for bill in bills_db:
        if bill.id == bill_id:
            return bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.put("/{bill_id}", response_model=BillRead)
async def update_bill(bill_id: int, updated_data: BillUpdate):
    for index, existing_bill in enumerate(bills_db):
        if existing_bill.id == bill_id:
            updated_bill = existing_bill.copy(
                update=updated_data.dict(exclude_unset=True)
            )
            bills_db[index] = updated_bill
            return updated_bill
    raise HTTPException(status_code=404, detail="Bill not found")

@router.delete("/{bill_id}")
async def delete_bill(bill_id: int):
    for index, existing_bill in enumerate(bills_db):
        if existing_bill.id == bill_id:
            del bills_db[index]
            return {"message": "Bill deleted"}
    raise HTTPException(status_code=404, detail="Bill not found")