# language: python
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from fast_api.db.db import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, default="Default Account")
    balance = Column(Float, default=0)

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    due_date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    paid = Column(Integer, default=0)  # Alternatively use Boolean

class Spending(Base):
    __tablename__ = "spendings"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account")

class Savings(Base):
    __tablename__ = "savings"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account")

class Income(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account")