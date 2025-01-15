from typing import TYPE_CHECKING
# from sqlalchemy import BIGINT
from sqlmodel import Field, SQLModel
from datetime import datetime

if TYPE_CHECKING:
    from .hr_employee import HREmployee


class AttPunchesBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    employee_id: int | None = Field(default=None, foreign_key="hr_employee.id")
    punch_time: datetime
    workcode: int | None = None
    workstate: int | None = None
    verifycode: str | None = None
    terminal_id: int | None = None
    punch_type: str | None = None
    operator: str | None = None
    operator_reason: str | None = None
    operator_time: datetime | None = None
    IsSelect: int | None = None
    reserved1: str | None = None
    reserved2: str | None = None
    middleware_id: int | None = None
    attendance_event: str | None = None
    login_combination: int | None = None
    status: int | None = None
    annotation: str | None = None
    processed: int | None = None


class AttPunchesCreate(AttPunchesBase):
    pass


class AttPunchesUpdate(AttPunchesBase):
    employee_id: int | None = None
    punch_time: datetime | None = None


class AttPunches(AttPunchesBase, table=True):
    __tablename__ = "att_punches"
    # id: int | None = Field(default=None, primary_key=True)
