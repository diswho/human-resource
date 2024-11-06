from typing import Any
from app.models.hr_employee import HREmployee, HREmployeesOut
from fastapi import APIRouter
from sqlmodel import select, func
from app.api.deps import SessionDep

router = APIRouter()


@router.get("/", response_model=HREmployeesOut)
def get_employees(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    count_statement = select(func.count()).select_from(HREmployee)
    count = session.exec(count_statement).one()
    statement = select(HREmployee).offset(skip).limit(limit)
    employees = session.exec(statement).all()
    return HREmployeesOut(data=employees, count=count)
