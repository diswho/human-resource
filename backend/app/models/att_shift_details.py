from datetime import datetime
from sqlmodel import SQLModel, Field, Integer
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .att_shift import AttShift


class AttShiftDetailsBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    shift_date: datetime
    dayTypeCode: int | None = None
    timetable_paycode: int | None = None
    shift_id: int | None = Field(default=None, foreign_key="att_shift.id")
    timetable_id: int | None = Field(default=None, foreign_key="att_timetable.id")


class AttShiftDetailsCreate(AttShiftDetailsBase):
    pass


class AttShiftDetailsUpdate(AttShiftDetailsBase):
    shift_date: datetime | None = None

# Set table name and foreign key constraint


class AttShiftDetails(AttShiftDetailsBase, table=True):
    __tablename__ = "att_shift_details"
    # id: int | None = Field(default=None, primary_key=True)
    # shift_id: int | None = Field(default=None, foreign_key="att_shift.id")
    # timetable_id: int | None = Field(default=None, foreign_key="att_timetable.id")
