# from sqlalchemy import DateTime
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# AttEmployeeShift


class AttEmployeeShiftBase(SQLModel):
    startDate: datetime
    endDate: datetime
    employee_id: int
    shift_id: int
    modifyDate: datetime | None = None
    NoEndDate: bool | None = None


class AttEmployeeShiftCreate(AttEmployeeShiftBase):
    pass


class AttEmployeeShiftUpdate(AttEmployeeShiftBase):
    startDate: datetime | None = None
    endDate: datetime | None = None
    employee_id: int | None = None
    shift_id: int | None = None

# Set table name and foreign key constraint


class AttEmployeeShift(AttEmployeeShiftBase, table=True):
    __tablename__ = "att_employee_shift"
    id: int | None = Field(default=None, primary_key=True)
    shift_id: int | None = Field(default=None, foreign_key="att_shift.id")
    startDate: datetime
    endDate: datetime
