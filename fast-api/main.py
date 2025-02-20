from fastapi import FastAPI
from routers import income
from routers import savings
app = FastAPI()

app.include_router(income.router, prefix="/incomes", tags=["Incomes"])
app.include_router(savings.router, prefix="/savings", tags=["Savings"])


@app.get("/")
def read_root():
    return {"message": "Hello World!"}