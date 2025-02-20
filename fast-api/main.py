from fastapi import FastAPI
from routers import income
from routers import savings
from routers import spending
from routers import bill

app = FastAPI()

app.include_router(income.router, prefix="/incomes", tags=["Incomes"])
app.include_router(savings.router, prefix="/savings", tags=["Savings"])
app.include_router(spending.router, prefix="/spendings", tags=["Spending"])
app.include_router(bill.router, prefix="/bills", tags=["Bill"])




@app.get("/")
def read_root():
    return {"message": "Hello World!"}