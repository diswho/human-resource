from sqlmodel import SQLModel, Field


class AttDayTypeBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    dt_code: int | None = None
    dt_desc: str | None = None
    export_code: str | None = None
    sign: str | None = None


class AttDayType(AttDayTypeBase, table=True):
    __tablename__ = "att_DayType"


class AttDayTypeCreate(AttDayTypeBase):
    pass


class AttDayTypeUpdate(AttDayTypeBase):
    dt_code: int | None = None
    dt_desc: str | None = None
    export_code: str | None = None
    sign: str | None = None
