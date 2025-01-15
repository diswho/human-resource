from sqlalchemy import Numeric
from sqlmodel import SQLModel, Field


class HRPerformanceBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    performance_period: str = Field(max_length=20)
    diligence: int
    meal_allowance: float = Field(sa_column=Numeric(10, 2))


class HRPerformance(HRPerformanceBase, table=True):
    __tablename__ = 'hr_performance'
