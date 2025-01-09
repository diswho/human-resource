from sqlmodel import SQLModel, Field
from datetime import date
from sqlalchemy import Numeric


class HRDeductionBase(SQLModel):
    deduction_date: date
    amount: float = Field(sa_column=Numeric(10, 2))


class HRDeduction(HRDeductionBase, table=True):
    __tablename__ = 'hr_deductions'
    deduction_id: int | None = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    deduction_type: int = Field(foreign_key="deduction_types.id")
