import uuid
from sqlmodel import Field, SQLModel


class SyNonMonthlyIncome(SQLModel):
    employee_id: int = Field(foreign_key='hr_employee.id')
    amount: float
    IssueDate: str = Field(max_length=50)
    type: int | None = Field(default=None, foreign_key='sy_type.id')
    status: int | None = Field(default=None, foreign_key='sy_status.id')


class SyNonMonthlyIncomeBase(SyNonMonthlyIncome, table=True):
    __tablename__ = 'sy_non_monthly_income'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
