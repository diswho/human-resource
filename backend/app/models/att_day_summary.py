from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime
from decimal import Decimal


class AttDaySummaryBase(SQLModel):
    att_date: datetime
    item_results: Decimal
    recordsFrom: datetime
    recordsTo: datetime
    iuser1: int | None = None
    iuser2: int | None = None
    iuser3: int | None = None
    cuser1: str | None = None
    cuser2: str | None = None
    cuser3: str | None = None
    remark: str | None = None
    dt_id: int | None = None
    item_id: int | None = None
    employee_id: int | None = None
    timetable_id: int | None = None
    paycode_id: int | None = None


class AttDaySummaryCreate(AttDaySummaryBase):
    pass


class AttDaySummaryUpdate(AttDaySummaryBase):
    att_date: datetime | None = None
    item_results: Decimal | None = None
    recordsFrom: datetime | None = None
    recordsTo: datetime | None = None
    item_id: int | None = None
    dt_id: int | None = None


class AttDaySummary(AttDaySummaryBase, table=True):
    __tablename__ = "att_day_summary"
    id: int | None = Field(default=None, primary_key=True)
    dt_id: int | None = Field(default=None, foreign_key="att_DayType.id")
    item_id: int | None = Field(default=None, foreign_key="att_StatisticItem.id")
    employee_id: int | None = Field(default=None, foreign_key="hr_employee.id")


class AttDaySummaryPublic(AttDaySummaryUpdate):
    pass


class AttDaySummariesPublic(SQLModel):
    data: list[AttDaySummaryPublic]
    count: int
