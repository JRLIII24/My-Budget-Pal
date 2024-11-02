# main.py
from fastapi import FastAPI
from routers import expenses, income, bills

app = FastAPI()

app.include_router(expenses.router)
app.include_router(income.router)
app.include_router(bills.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Budgeting API"}