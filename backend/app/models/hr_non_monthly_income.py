import uuid
from sqlmodel import Field, SQLModel


class HrNonMonthlyIncome(SQLModel, table=True):
    employee_id: int = Field(foreign_key='hr_employee.id')
    amount: float
    type: str = Field(max_length=50)
    Status: str = Field(max_length=50)
    IssueDate: str = Field(max_length=50)


class HrNonMonthlyIncomeBase(HrNonMonthlyIncome, table=True):
    __tablename__ = 'hr_non_monthly_income'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
