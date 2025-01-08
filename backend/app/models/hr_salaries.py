from sqlmodel import Field, SQLModel
from datetime import date
from decimal import Decimal
from sqlmodel import Relationship
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .hr_employee import HREmployee


class HRSalaryBase(SQLModel):
    salary_date: date | None = None
    base_salary: Decimal | None = None
    fuel_allowance: Decimal | None = None
    risk_allowance: Decimal | None = None


class HRSalary(HRSalaryBase, table=True):
    __tablename__ = 'hr_salaries'

    id: int | None = Field(default=None, primary_key=True)
    employee_id: int | None = Field(default=None, foreign_key='hr_employee.id')
    employee: Optional["HREmployee"] = Relationship(back_populates="salaries")
