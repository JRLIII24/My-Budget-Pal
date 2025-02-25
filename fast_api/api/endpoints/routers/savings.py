from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fast_api.db import crud, schemas, db
router = APIRouter()

@router.post("/", response_model=schemas.SavingsResponse)
def create_savings(savings: schemas.SavingsCreate, session: Session = Depends(db.get_db)):
    try:
        return crud.create_savings(db=session, savings=savings)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.SavingsResponse])
def read_savings(session: Session = Depends(db.get_db)):
    savings_list = crud.get_all_savings(db=session)
    return savings_list

@router.get("/{savings_id}", response_model=schemas.SavingsResponse)
def read_savings_item(savings_id: int, session: Session = Depends(db.get_db)):
    savings_item = crud.get_savings(db=session, savings_id=savings_id)
    if not savings_item:
        raise HTTPException(status_code=404, detail="Savings item not found")
    return savings_item

@router.put("/{savings_id}", response_model=schemas.SavingsResponse)
def update_savings(savings_id: int, savings: schemas.SavingsCreate, session: Session = Depends(db.get_db)):
    updated_savings = crud.update_savings(db=session, savings_id=savings_id, savings=savings)
    if not updated_savings:
        raise HTTPException(status_code=404, detail="Savings item not found")
    return updated_savings

@router.delete("/{savings_id}", response_model=schemas.SavingsResponse)
def delete_savings(savings_id: int, session: Session = Depends(db.get_db)):
    deleted_savings = crud.delete_savings(db=session, savings_id=savings_id)
    if not deleted_savings:
        raise HTTPException(status_code=404, detail="Savings item not found")
    return deleted_savings