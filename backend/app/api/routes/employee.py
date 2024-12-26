from typing import Any, List, Optional
from app.models.hr_employee import HREmployee, HREmployeesOut
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, func
from app.api.deps import SessionDep
from sqlalchemy.dialects import postgresql
router = APIRouter()


@router.get("/", response_model=HREmployeesOut)
# def get_employees(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
def get_employees(session: SessionDep, skip: int = 0, limit: int = 100, descendants: Optional[List[int]] = Query(None)) -> Any:
    count_statement = select(func.count()).select_from(HREmployee)
    statement = select(HREmployee).offset(skip).limit(limit)       
  
    if descendants:
        count_statement = count_statement.where(HREmployee.department_id.in_(descendants))
        statement = statement.where(HREmployee.department_id.in_(descendants))
    
    count = session.exec(count_statement).one()
    employees = session.exec(statement).all()        
    return HREmployeesOut(data=employees, count=count)

@router.put("/{employee_id}", response_model=HREmployeesOut)
def update_employee(employee_id: int, employee_update: HREmployeesOut, session: SessionDep) -> Any:
    employee = session.get(HREmployee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    for key, value in employee_update.dict(exclude_unset=True).items():
        setattr(employee, key, value)
    
    session.add(employee)
    session.commit()
    session.refresh(employee)
    
    return employee