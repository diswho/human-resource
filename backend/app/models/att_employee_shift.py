from sqlmodel import SQLModel, Field,  DateTime
from typing import Optional

# AttEmployeeShift


class AttEmployeeShiftBase(SQLModel):
    startDate: DateTime
    endDate: DateTime
    employee_id: int
    shift_id: int
    modifyDate: DateTime | None = None
    NoEndDate: bool | None = None


class AttEmployeeShiftCreate(AttEmployeeShiftBase):
    pass


class AttEmployeeShiftUpdate(AttEmployeeShiftBase):
    startDate: DateTime | None = None
    endDate: DateTime | None = None
    employee_id: int | None = None
    shift_id: int | None = None

# Set table name and foreign key constraint


class AttEmployeeShift(AttEmployeeShiftBase, table=True):
    __tablename__ = "att_employee_shift"
    id: int | None = Field(default=None, primary_key=True)
    shift_id: int | None = Field(default=None, foreign_key="att_shift.id")
