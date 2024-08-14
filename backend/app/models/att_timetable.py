from sqlmodel import SQLModel, Field, Integer, Text, DateTime, Boolean
from typing import Optional

# AttTimetable

class AttTimetableBase(SQLModel):
    timetableType: int | None = None
    timetable_color: int | None = None
    timetable_name: str
    timetable_start: DateTime | None = None
    timetable_end: DateTime | None = None
    timetable_checkin_begin: DateTime | None = None
    timetable_checkout_end: DateTime | None = None
    usedForSmartShift: bool | None = None
    timetable_checkin_end: DateTime | None = None
    timetable_checkout_begin: DateTime | None = None
    requireWork: int | None = None
    timetable_late: bool | None = None
    timetable_latecome: int | None = None
    timetable_early: bool | None = None
    timetable_earlyout: int | None = None
    countAbsentLateExceed: bool | None = None
    countAbsentLateExceedMins: int | None = None
    withoutInAsLateAllDay: bool | None = None
    countAbsentEarlyExceed: bool | None = None
    countAbsentEarlyExceedMins: int | None = None
    withoutOutAsEarlyAllDay: bool | None = None
    enableOT: bool | None = None
    earlyComeAsWork: bool | None = None
    lateOutAsWork: bool | None = None
    firstInLastOut: bool | None = None
    isDefault: bool | None = None
    timetable_lateincluderelatives: bool | None = None
    countEarlyComeExceedMins: int | None = None
    countLateOutExceedMins: int | None = None

class AttTimetableCreate(AttTimetableBase):
    pass

class AttTimetableUpdate(AttTimetableBase):
    timetable_name: str | None = None

# Set table name
class AttTimetable(AttTimetableBase, table=True):
    __tablename__ = "att_timetable"
    id: int | None = Field(default=None, primary_key=True)

