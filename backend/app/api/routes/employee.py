from datetime import date
from typing import Any, List, Optional
from app.models.hr_employee import HREmployee, HREmployeesOut
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select, func
from app.api.deps import SessionDep
from sqlalchemy.dialects import postgresql
from app.models.hr_salaries import HRSalary, HRSalaryUpdate
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


@router.post("/new_salary", response_model=HRSalary)
def new_salary(salary_in: HRSalary, session: SessionDep) -> Any:
    # based on hr_salaries.py, build the logic to create a new salary record.
    # return the newly created salary record.
    salary=HRSalary.model_validate(salary_in)
    session.add(salary)
    session.commit()
    session.refresh(salary)
    return salary


@router.put("/update_salary/{employee_id}", response_model=HRSalaryUpdate)
def update_employee_salary(*, session: SessionDep, employee_id: int, salary: HRSalaryUpdate) -> Any:
    # based on hr_salaries.py, build the logic to update the salary of an employee,
    # where input is the employee_id and date.
    # condition: if the salary date(Month-Year) is already present in the database, update the salary, else create a new salary record.
    # return the updated employee record.
    employee = session.get(HREmployee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    salary_date = date.today().replace(day=1)
    salary_record = session.exec(select(HRSalary).where(HRSalary.employee_id == employee_id, HRSalary.salary_date == salary_date)).first()

    if not salary_record:
        salary_record = HRSalary(employee_id=employee_id, salary_date=salary_date)

    salary_record.base_salary = salary
    session.add(salary_record)
    session.commit()
    session.refresh(employee)

    return employee
