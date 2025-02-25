from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fast_api.db import crud, schemas, db

router = APIRouter()

@router.post("/", response_model=schemas.SpendingResponse)
def create_spending(spending: schemas.SpendingCreate, session: Session = Depends(db.get_db)):
    try:
        return crud.create_spending(db=session, spending=spending)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.SpendingResponse])
def read_spendings(session: Session = Depends(db.get_db)):
    spendings = crud.get_all_spendings(db=session)
    return spendings

@router.get("/{spending_id}", response_model=schemas.SpendingResponse)
def read_spending(spending_id: int, session: Session = Depends(db.get_db)):
    spending = crud.get_spending(db=session, spending_id=spending_id)
    if not spending:
        raise HTTPException(status_code=404, detail="Spending not found")
    return spending

@router.put("/{spending_id}", response_model=schemas.SpendingResponse)
def update_spending(spending_id: int, spending: schemas.SpendingCreate, session: Session = Depends(db.get_db)):
    updated_spending = crud.update_spending(db=session, spending_id=spending_id, spending=spending)
    if not updated_spending:
        raise HTTPException(status_code=404, detail="Spending not found")
    return updated_spending

@router.delete("/{spending_id}", response_model=schemas.SpendingResponse)
def delete_spending(spending_id: int, session: Session = Depends(db.get_db)):
    deleted_spending = crud.delete_spending(db=session, spending_id=spending_id)
    if not deleted_spending:
        raise HTTPException(status_code=404, detail="Spending not found")
    return deleted_spending