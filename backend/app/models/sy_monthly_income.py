import uuid
from app.models.sy_status import SyStatus
from app.models.sy_type import SyType
from sqlmodel import Field, SQLModel


class SyMonthlyIncome(SQLModel):
    employee_id: int = Field(foreign_key='hr_employee.id')
    amount: float
    type: SyType = Field(default_factory=SyType.ADVANCE, sa_column_kwargs={"type": "VARCHAR(50)"})
    Status: SyStatus = Field(default_factory=SyStatus.INITIATED, sa_column_kwargs={"type": "VARCHAR(50)"})
    IssueDate: str = Field(max_length=50)
    FromDate: str = Field(max_length=50)
    ToDate: str = Field(max_length=50)
    Accumulated: float
    Total: float


class SyMonthlyIncomeBase(SyMonthlyIncome, table=True):
    __tablename__ = 'sy_monthly_income'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
