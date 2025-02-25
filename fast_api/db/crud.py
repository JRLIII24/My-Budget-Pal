from sqlalchemy.orm import Session
from fast_api.db import models, schemas

def get_or_create_account(db: Session, name: str = "Default Account"):
    """Retrieve the default account or create one if it does not exist."""
    account = db.query(models.Account).first()
    if not account:
        account = models.Account(name=name, balance=0.0)
        db.add(account)
        db.commit()
        db.refresh(account)
    return account

def create_income(db: Session, income: schemas.IncomeCreate):
    """Create an income entry and update the account balance."""
    account = get_or_create_account(db)
    db_income = models.Income(**income.dict(), account_id=account.id)
    db.add(db_income)
    account.balance += income.amount
    db.commit()
    db.refresh(db_income)
    return db_income

def create_savings(db: Session, savings: schemas.SavingsCreate):
    """Create a savings entry and deduct the amount from the account balance."""
    account = get_or_create_account(db)
    if account.balance < savings.amount:
        raise ValueError("Insufficient funds")
    db_savings = models.Savings(**savings.dict(), account_id=account.id)
    db.add(db_savings)
    account.balance -= savings.amount
    db.commit()
    db.refresh(db_savings)
    return db_savings

def create_spending(db: Session, spending: schemas.SpendingCreate):
    """Create a spending entry and deduct the amount from the account balance."""
    account = get_or_create_account(db)
    if account.balance < spending.amount:
        raise ValueError("Insufficient funds")
    db_spending = models.Spending(**spending.dict(), account_id=account.id)
    db.add(db_spending)
    account.balance -= spending.amount
    db.commit()
    db.refresh(db_spending)
    return db_spending

def create_bill(db: Session, bill: schemas.BillCreate):
    """Create a bill entry."""
    account = get_or_create_account(db)
    db_bill = models.Bill(**bill.dict(), account_id=account.id)
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill