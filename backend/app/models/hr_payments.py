from sqlmodel import SQLModel, Field
from datetime import date
from sqlalchemy import Numeric


class HRPaymentBase(SQLModel):
    payment_id: int | None = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    payment_type: int = Field(foreign_key="payment_types.id")
    payment_date: date
    amount: float = Field(sa_column=Numeric(10, 2))


class HRPayment(HRPaymentBase, table=True):
    __tablename__ = 'hr_payments'
