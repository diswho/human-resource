import uuid
from sqlmodel import Field, SQLModel


class HrMonthlyOutcome(SQLModel):
    employee_id: int = Field(foreign_key='hr_employee.id')
    amount: float
    type: str = Field(max_length=50)
    Status: str = Field(max_length=50)
    IssueDate: str = Field(max_length=50)
    FromDate: str = Field(max_length=50)
    ToDate: str = Field(max_length=50)
    Accumulated: float
    Total: float


class HrMonthlyOutcomeBase(HrMonthlyOutcome, table=True):
    __tablename__ = 'hr_monthly_outcome'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
