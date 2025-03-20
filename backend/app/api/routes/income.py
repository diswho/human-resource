from app import crud
from app.api.deps import SessionDep
from app.models.sy_monthly_income import (
    MonthlyIncomeBase,
    MonthlyIncomeCreate,
    MonthlyIncomePublic,
)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from sqlmodel import select

router = APIRouter()


@router.post("/monthly_income/{employee_id}", response_model=MonthlyIncomePublic)
async def create_monthly_income(*, session: SessionDep, income: MonthlyIncomeCreate):
    statement = select(MonthlyIncomeBase).where(
        MonthlyIncomeBase.employee_id == income.employee_id,
        MonthlyIncomeBase.type == income.type,
    )
    incomes = session.exec(statement).first()
    monthly_incomes = crud.create_monthly_income(
        session=session, monthly_income_create=income
    )
    # if monthly_incomes:
    return monthly_incomes


@router.get("/monthly_income/{employee_id}", response_model=List[MonthlyIncomePublic])
async def get_monthly_income_by_employee(employee_id: int):
    employee_incomes = [
        income for income in MonthlyIncomePublic if income.employee_id == employee_id
    ]
    if not employee_incomes:
        raise HTTPException(
            status_code=404, detail="Monthly income not found for the given employee ID"
        )
    return employee_incomes
