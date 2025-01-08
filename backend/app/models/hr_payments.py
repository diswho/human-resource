from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from datetime import date

if TYPE_CHECKING:
    from .hr_employee import HREmployee


class HRPaymentBase(SQLModel):
    payment_date: date
    amount: float = Field(sa_column_kwargs={"decimal_places": 2, "max_digits": 10})


class HRPayment(HRPaymentBase, table=True):
    __tablename__ = 'hr_payments'
    payment_id: int | None = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    payment_type: int = Field(foreign_key="payment_types.id")
    employee: Optional["HREmployee"] = Relationship(back_populates="payments")
