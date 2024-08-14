from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey
from sqlmodel import Field, SQLModel

if TYPE_CHECKING:
    from .company import HRCompany


class HRPositionBase(SQLModel):
    posi_code: int
    posi_name: str
    description: str | None = None
    posi_parentcode: int
    defaultPosition: int | None = None
    company_id: int | None = Field(default=None, foreign_key="hr_company.id")


class HRPosition(HRPositionBase, table=True):
    __tablename__ = "hr_position"
    id: int | None = Field(default=None, primary_key=True)


class HRPositionCreate(HRPositionBase):
    pass


class HRPositionUpdate(HRPositionBase):
    posi_code: int | None = None
    posi_name: str | None = None
    posi_parentcode: int | None = None
