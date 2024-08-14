from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .company import HRCompany


class HRDepartmentBase(SQLModel):
    dept_code: int
    dept_name: str
    dept_parentcode: int
    useCode: bool | None = None
    dept_operationmode: int | None = None
    defaultDepartment: int | None = None
    lineToken: str | None = None
    description: str | None = None


class HRDepartment(HRDepartmentBase, table=True):
    __tablename__ = "hr_department"
    id: int | None = Field(default=None, primary_key=True)
    company_id: int | None = Field(default=None, foreign_key="hr_company.id")
    company: "HRCompany" = Relationship(back_populates="departments")


class HRDepartmentCreate(HRDepartmentBase):
    company_id: int = Field(default=None, foreign_key="hr_company.id")
    company: "HRCompany" = Relationship(back_populates="departments")


class HRDepartmentUpdate(HRDepartmentBase):
    dept_code: int | None = None
    dept_name: str | None = None
    dept_parentcode: int | None = None
    company_id: int | None = None
