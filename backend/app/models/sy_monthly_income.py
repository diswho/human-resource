import uuid
from sqlmodel import Field, SQLModel


class SyMonthlyIncome(SQLModel):
    employee_id: int = Field(foreign_key="hr_employee.id")
    amount: float
    IssueDate: str = Field(max_length=50)
    FromDate: str = Field(max_length=50)
    ToDate: str = Field(max_length=50)
    Accumulated: float
    Total: float
    type: int | None = Field(default=None, foreign_key="sy_type.id")
    status: int | None = Field(default=None, foreign_key="sy_status.id")


class MonthlyIncomeBase(SyMonthlyIncome, table=True):
    __tablename__ = "sy_monthly_income"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class MonthlyIncomeCreate(MonthlyIncomeBase):
    employee_id: int
    amount: float
    IssueDate: str
    FromDate: str
    ToDate: str
    Accumulated: float
    Total: float
    type: int | None = None
    status: int | None = None


class MonthlyIncomePublic(MonthlyIncomeBase):
    id: uuid.UUID
    employee_id: int
    amount: float
    IssueDate: str
    FromDate: str
    ToDate: str
    Accumulated: float
    Total: float
    type: int | None
    status: int | None
