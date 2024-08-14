from typing import TYPE_CHECKING
from sqlmodel import Field, SQLModel, Numeric, ForeignKey, Column
from datetime import datetime
from decimal import Decimal

if TYPE_CHECKING:
    from .position import HRPosition
    from .department import HRDepartment


class HREmployeeBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None
    emp_pin: str | None = None
    emp_ssn: str | None = None
    emp_role: str | None = None
    emp_firstname: str | None = None
    emp_lastname: str | None = None
    emp_username: str | None = None
    emp_pwd: str | None = None
    emp_timezone: str | None = None
    emp_phone: str | None = None
    emp_payroll_id: str | None = None
    emp_payroll_type: str | None = None
    emp_pin2: str | None = None
    emp_photo: bytes | None = None
    emp_privilege: str | None = None
    emp_group: str | None = None
    emp_hiredate: datetime | None = None
    emp_address: str | None = None
    emp_active: int | None = None
    emp_firedate: datetime | None = None
    emp_firereason: str | None = None
    emp_emergencyphone1: str | None = None
    emp_emergencyphone2: str | None = None
    emp_emergencyname: str | None = None
    emp_emergencyaddress: str | None = None
    emp_cardNumber: str | None = None
    emp_country: str | None = None
    emp_city: str | None = None
    emp_state: str | None = None
    emp_postal: str | None = None
    emp_fax: str | None = None
    emp_title: str | None = None
    emp_hourlyrate1: Decimal | None = None
    emp_hourlyrate2: Decimal | None = None
    emp_hourlyrate3: Decimal | None = None
    emp_hourlyrate4: Decimal | None = None
    emp_hourlyrate5: Decimal | None = None
    emp_gender: int | None = None
    emp_birthday: datetime | None = None
    emp_operationmode: int | None = None
    emp_OtherName: str | None = None
    emp_Line: str | None = None
    emp_Passport: str | None = None
    emp_MotobikeLicence: str | None = None
    emp_CarLicence: str | None = None
    emp_customName1: str | None = None
    emp_customInfo1: str | None = None
    emp_customName2: str | None = None
    emp_customInfo2: str | None = None
    IsSelect: int | None = None
    nationalID: str | None = None
    emp_Verify: str | None = None
    emp_ViceCard: str | None = None
    department_id: int | None = Field(default=None, foreign_key="hr_department.id")
    position_id: int | None = Field(default=None, foreign_key="hr_position.id")


class HREmployee(HREmployeeBase, table=True):
    __tablename__ = "hr_employee"
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str


class HREmployeeCreate(HREmployeeBase):
    password: str


class HREmployeeCreateOpen(SQLModel):
    email: str
    password: str
    full_name: str | None = None


class HREmployeeUpdate(HREmployeeBase):
    email: str | None = None  # type: ignore
    password: str | None = None


class HREmployeeUpdateMe(HREmployeeBase):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


class HREmployeeOut(HREmployeeBase):
    id: int


class HREmployeesOut(SQLModel):
    data: list[HREmployeeOut]
    count: int
