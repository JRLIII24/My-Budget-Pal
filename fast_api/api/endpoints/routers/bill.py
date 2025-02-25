from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fast_api.db import crud, schemas, db
router = APIRouter()

@router.post("/", response_model=schemas.BillResponse)
def create_bill(bill: schemas.BillCreate, session: Session = Depends(db.get_db)):
    try:
        return crud.create_bill(db=session, bill=bill)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.BillResponse])
def read_bills(session: Session = Depends(db.get_db)):
    bills = crud.get_all_bills(db=session)
    return bills

@router.get("/{bill_id}", response_model=schemas.BillResponse)
def read_bill(bill_id: int, session: Session = Depends(db.get_db)):
    bill = crud.get_bill(db=session, bill_id=bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill

@router.put("/{bill_id}", response_model=schemas.BillResponse)
def update_bill(bill_id: int, bill: schemas.BillCreate, session: Session = Depends(db.get_db)):
    updated_bill = crud.update_bill(db=session, bill_id=bill_id, bill=bill)
    if not updated_bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return updated_bill

@router.delete("/{bill_id}", response_model=schemas.BillResponse)
def delete_bill(bill_id: int, session: Session = Depends(db.get_db)):
    deleted_bill = crud.delete_bill(db=session, bill_id=bill_id)
    if not deleted_bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return deleted_bill