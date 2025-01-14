from sqlmodel import Field, SQLModel
from datetime import date
from decimal import Decimal


class HRSalaryBase(SQLModel):
    salary_date: date 
    base_salary: Decimal 
    fuel_allowance: Decimal 
    risk_allowance: Decimal 

class HRSalary(HRSalaryBase, table=True):
    __tablename__ = 'hr_salaries'
    id: int | None = Field(default=None, primary_key=True)
    employee_id: int | None = Field(default=None, foreign_key='hr_employee.id')


class HRSalaryUpdate(HRSalaryBase):
    employee_id: int 
    salary_date: date | None = Field(default=None)
    base_salary: Decimal | None = Field(default=None)
    fuel_allowance: Decimal | None = Field(default=None)
    risk_allowance: Decimal | None = Field(default=None)
