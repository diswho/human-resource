from typing import TYPE_CHECKING, Any, Dict, List, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .hr_company import HRCompany


class HRDepartmentBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    dept_code: int
    dept_name: str
    dept_parentcode: int
    useCode: int | None = None
    dept_operationmode: int | None = None
    defaultDepartment: int | None = None
    company_id: int | None = Field(default=None, foreign_key="hr_company.id")
    lineToken: str | None = None
    description: str | None = None


class HRDepartment(HRDepartmentBase, table=True):
    __tablename__ = "hr_department"
    # id: int | None = Field(default=None, primary_key=True)
    # company_id: int | None = Field(default=None, foreign_key="hr_company.id")
    # company: "HRCompany" = Relationship(back_populates="departments")


class HRDepartmentCreate(HRDepartmentBase):
    # company_id: int = Field(default=None, foreign_key="hr_company.id")
    # company: "HRCompany" = Relationship(back_populates="departments")
    pass


class HRDepartmentUpdate(HRDepartmentBase):
    dept_code: int | None = None
    dept_name: str | None = None
    dept_parentcode: int | None = None
    company_id: int | None = None


class HRDepartmentExport(SQLModel):
    id: int
    dept_code: int
    dept_name: str
    dept_parentcode: int
    # children: Dict[int, HRDepartment]
    descendants: List[int]
    level: int


class HRDepartmentPublic(SQLModel):
    id: int
    dept_code: int
    dept_name: str
    dept_parentcode: int
    # children: Dict[int, HRDepartmentExport]
    descendants: List[int]
    level: int


class HRDepartmentOut(HRDepartmentPublic):
    id: int


class HRDepartmentsOut(SQLModel):
    data: List[HRDepartmentOut]
    count: int
