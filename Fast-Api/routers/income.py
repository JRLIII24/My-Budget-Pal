from fastapi import APIRouter
from models import Income

router = APIRouter()

incomes = []
income_id_count = 1