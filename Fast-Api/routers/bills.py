from fastapi import APIRouter
from models import Bill

router = APIRouter()

bills = []
bills_id_count = 1

@router.post("/bills/", response_model=Bill)
async def create_bill(bill: Bill):
    global bills_id_count
    bill.id= bills_id_count
    bills.append(bill)
    bills_id_count += 1
    return bill