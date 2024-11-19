from fastapi import FastAPI
from models import Base
from routers import expenses, income, bills
from database import database, metadata, engine

app = FastAPI()

app.include_router(expenses.router)
app.include_router(income.router)
app.include_router(bills.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Budgeting API"}

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()