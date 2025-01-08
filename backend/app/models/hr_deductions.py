from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from datetime import date

if TYPE_CHECKING:
    from .hr_employee import HREmployee


class HRDeductionBase(SQLModel):
    deduction_date: date
    amount: float = Field(sa_column_kwargs={"decimal_places": 2, "max_digits": 10})


class HRDeduction(HRDeductionBase, table=True):
    __tablename__ = 'hr_deductions'
    deduction_id: int | None = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    deduction_type: int = Field(foreign_key="deduction_types.id")
    employee: Optional["HREmployee"] = Relationship(back_populates="deductions")
