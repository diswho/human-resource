from sqlmodel import SQLModel, Field, Text, Boolean,  Integer
from typing import Optional
from datetime import datetime

# AttShift


class AttShiftBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    shift_name: str
    cycle_available: bool
    cycle_type: int | None = None
    cycle_parameter: int | None = None
    start_date: datetime | None = None
    defaultShift: bool | None = None


class AttShiftCreate(AttShiftBase):
    pass


class AttShiftUpdate(AttShiftBase):
    shift_name: str | None = None
    cycle_available: bool | None = None

# Set table name


class AttShift(AttShiftBase, table=True):
    __tablename__ = "att_shift"
    # id: int | None = Field(default=None, primary_key=True)
