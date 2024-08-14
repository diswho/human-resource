from sqlmodel import SQLModel, Field, Integer, DateTime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .att_shift import AttShift

class AttShiftDetailsBase(SQLModel):
    shift_date: DateTime
    dayTypeCode: int | None = None
    timetable_paycode: int | None = None
    timetable_id: int | None = None

class AttShiftDetailsCreate(AttShiftDetailsBase):
    pass

class AttShiftDetailsUpdate(AttShiftDetailsBase):
    shift_date: DateTime | None = None

# Set table name and foreign key constraint
class AttShiftDetails(AttShiftDetailsBase, table=True):
    __tablename__ = "att_shift_details"
    id: int | None = Field(default=None, primary_key=True)
    shift_id: int | None = Field(default=None, foreign_key="att_shift.id")
    timetable_id: int | None = Field(default=None, foreign_key="att_timetable.id")
