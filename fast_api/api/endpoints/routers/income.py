from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fast_api.db import crud, schemas, db

router = APIRouter()

@router.post("/", response_model=schemas.IncomeResponse)
def create_income(income: schemas.IncomeCreate, session: Session = Depends(db.get_db)):
    try:
        return crud.create_income(db=session, income=income)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.IncomeResponse])
def read_incomes(session: Session = Depends(db.get_db)):
    incomes = crud.get_all_incomes(db=session)
    return incomes

@router.get("/{income_id}", response_model=schemas.IncomeResponse)
def read_income(income_id: int, session: Session = Depends(db.get_db)):
    income = crud.get_income(db=session, income_id=income_id)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@router.put("/{income_id}", response_model=schemas.IncomeResponse)
def update_income(income_id: int, income: schemas.IncomeCreate, session: Session = Depends(db.get_db)):
    updated_income = crud.update_income(db=session, income_id=income_id, income=income)
    if not updated_income:
        raise HTTPException(status_code=404, detail="Income not found")
    return updated_income

@router.delete("/{income_id}", response_model=schemas.IncomeResponse)
def delete_income(income_id: int, session: Session = Depends(db.get_db)):
    deleted_income = crud.delete_income(db=session, income_id=income_id)
    if not deleted_income:
        raise HTTPException(status_code=404, detail="Income not found")
    return deleted_income