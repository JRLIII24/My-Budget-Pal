from fastapi import FastAPI

# Corrected imports for the routers
from fast_api.api.endpoints.routers import income, savings, spending, bill

# Corrected imports for database connection and models
from fast_api.db.db import engine, Base
from fast_api.db import models

# Ensure database tables are created
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers for different budget components
app.include_router(income.router, prefix="/incomes", tags=["Income"])
app.include_router(savings.router, prefix="/savings", tags=["Savings"])
app.include_router(spending.router, prefix="/spendings", tags=["Spending"])
app.include_router(bill.router, prefix="/bills", tags=["Bills"])