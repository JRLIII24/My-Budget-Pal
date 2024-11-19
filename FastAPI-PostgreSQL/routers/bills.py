from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Bill as BillDB
from pydantic_models import Bill
from typing import List

router = APIRouter()

@router.post("/bills/", response_model=Bill)
async def create_bill(bill: Bill, db: Session = Depends(get_db)):
    new_bill = BillDB(
        name=bill.name,
        amount=bill.amount,
        due_date=bill.due_date,
    )
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill

# Get all bills
@router.get("/bills/", response_model=List[Bill])
async def get_bills(db: Session = Depends(get_db)):
    return db.query(BillDB).all()

@router.get("/bills/{bill_id}", response_model=Bill)
async def get_bill_id(bill_id: int, db: Session = Depends(get_db)):
    bill = db.query(BillDB).filter(BillDB.id == bill_id).first()
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill

@router.put("/bills/{bill_id}", response_model=Bill)
async def update_bill(bill_id: int, bill: Bill, db: Session = Depends(get_db)):
    existing_bill = db.query(BillDB).filter(BillDB.id == bill_id).first()
    if not existing_bill:
        raise HTTPException(status_code=404, detail="Bill not found")

    existing_bill.name = bill.name
    existing_bill.amount = bill.amount
    existing_bill.due_date = bill.due_date
    db.commit()
    db.refresh(existing_bill)
    return existing_bill

@router.delete("/bills/{bill_id}")
async def delete_bill(bill_id: int, db: Session = Depends(get_db)):
    bill = db.query(BillDB).filter(BillDB.id == bill_id).first()
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    db.delete(bill)
    db.commit()
    return {"message": "Bill successfully deleted"}