from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from datetime import date

if TYPE_CHECKING:
    from .hr_employee import HREmployee


class HRPerformanceBase(SQLModel, table=True):
    performance_period: str = Field(max_length=20)
    diligence: int
    meal_allowance: float = Field(sa_column_kwargs={"decimal_places": 2, "max_digits": 10})


class HRPerformance(HRPerformanceBase, table=True):
    __tablename__ = 'hr_performance'
    performance_id: int = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="hr_employee.id")
    employee: Optional["HREmployee"] = Relationship(back_populates="performances")
